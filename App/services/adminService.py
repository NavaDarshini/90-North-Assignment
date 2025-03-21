from email import message
from shutil import ExecError
from tabnanny import check
from unicodedata import category
from App.models.permissionModel import PermissionModel
from App.utils import messages
from App.models.talentCategoryModel import TalentCategoryModel
from App.models.talentSubCategoryModel import TalentSubCategoryModel
from App.serializers import adminSerializer
from App.models.faqModel import FAQModel
from App.models import TermAndConditionModel
from django.contrib.auth.hashers import check_password, make_password
from App.serializers.adminSerializer import TermAndConditionsSerializer
from App.models import UserModel
from rest_framework_simplejwt.tokens import RefreshToken
from App.utils.sendOtp import send_otp_via_mail,make_otp,generate_password,\
                                     send_password_via_mail, generate_encoded_id,\
                                         send_notification_to_mail
from App.models import ManageAddressModel
from App.models.talentDetailsModel import TalentDetailsModel
from App.models.bookingTalentModel import BookingTalentModel
from App.utils.customPagination import CustomPagination
from threading import Thread
from django.utils import timezone
from App.models import userModel, NotificationModel
from pyfcm import FCMNotification
from App.models.contactUsModel import ContactUsModel
from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from App.serializers.Clientserializer import ShowBookingDetailsSerializer
from App.models.ratingsModel import ReviewAndRatingsModel 
from django.http import HttpResponse
import csv
import calendar
from App.models.colourPreferencesModel import ColourPreferencesModel

class AdminService:
    def add_category(self, request):
        # name = request.data["name"]
        # talent_obj = TalentCategoryModel.objects.create(name=name)
        try:
            data = TalentCategoryModel.objects.filter(name =request.data["name"])
            if data:
                return {"data":None,"message":"Category already exist","status":400}
            serializer =adminSerializer.CategorySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return {"data": request.data, "message": messages.CATEGORY_ADDED, "status": 201}
            else:
                return {"data": None, "message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}
    
    def add_sub_category(self, request):
        try:
            data = TalentSubCategoryModel.objects.filter(name =request.data["name"])
            if data:
                return {"data":None,"message":"Sub-category already exist","status":400}
            serializers = adminSerializer.SubCategorySerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return {"data": serializers.data, "message": messages.SUB_CATEGORY_ADDED, "status": 201}
            else:
                return {"data": None, "message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}
        # name = request.data["name"]
        # category_id = request.data["category"]
        # talent_sub_category = TalentSubCategoryModel.objects.create(
        #     name=name,
        #     category_id=category_id
        # )
    
    def subcategory_listing_by_category_id(self, request):
        sub_categories = TalentSubCategoryModel.objects.filter(category = request.data["category"])
        serializer = adminSerializer.SubCategorySerializer(sub_categories, many=True)
        return {"data": serializer.data, "message": messages.SUB_CATEGORIES_LISTING, "status": 200}
    
    def add_questions_answers(self, request):
        serializers = adminSerializer.FAQSerializer(data=request.data)
        try:
            if serializers.is_valid():
                serializers.save()
            return {"data":serializers.data,"message":messages.ADD,"status":200}
        except Exception as e:
            return {"data": None, "message":str(e),"status":400}
            

    def update_questions_answers(self, request, id):
        questions = FAQModel.objects.get(id=id)
        try:
            serializers = adminSerializer.FAQSerializer(questions,data = request.data)
            if serializers.is_valid():
                serializers.save()
                return {"data":serializers.data,"message":messages.UPDATE,"status":200}
            else:
                return {"data": None, "message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"message":str(e),"status":400}

    def delete_question_answer(self, request, id):
        try:
            question = FAQModel.objects.get(id=id)
            question.delete()
            return {"data": None, "message":messages.DELETE, "status":200}
        except Exception as e:
            return {"data": None, "message":str(e), "status":400}
    
    def get_all_questions_answers(self , request):
        try:
            questions = FAQModel.objects.all()
            pagination_obj = CustomPagination()
            search_keys = ["question__icontains"]
            result = pagination_obj.custom_pagination(request, search_keys, \
                                                      adminSerializer.FAQSerializer, questions)
            # serializer = adminSerializer.GetAllClientsDetailsSerializer(clients, many=True)
            return {
                        "data":result["response_object"],
                        "total_records": result["total_records"],
                        "start": result["start"],
                        "length": result["length"], 
                        "message":messages.USER_DETAILS_FETCHED, 
                        "status":200
                    }
            # serializers = adminSerializer.FAQSerializer(questions, many=True)
            # return {"data":serializers.data,"message":messages.QUESTION_FETCHED,"status":200}
        except Exception as e:
            return {"data":None, "message":str(e),"status":400}


    def get_question_by_id(self, request, id):
        try:
            data = FAQModel.objects.get(id=id)
        except Exception as e:
            return {"data":None,"messages":messages.NOT_FOUND,"status":400}
        serializer = adminSerializer.FAQSerializer(data)
        return {"data":serializer.data,"message":messages.FETCH,"status":200}



    #termsAndConditions
    def add_terms_and_conditions(self, request):
        try:
            terms = TermAndConditionModel.objects.filter(id = 1)
            if not terms:
                serializer = adminSerializer.TermAndConditionsSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"messages":messages.QUESTION_ADDED, "status":200}
                else:
                    return {"data":None, "message":messages.WENT_WRONG, "status":400}
            else:
                terms = TermAndConditionModel.objects.get(id = 1)
                serializer = adminSerializer.TermAndConditionsSerializer(terms, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"message":messages.ADD,"status":200}
                else:
                    return {"data":None,"message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data":None, "message":messages.WENT_WRONG, "status":400}

    def get_terms_and_conditions(self, request):
        try:
            terms = TermAndConditionModel.objects.all()
            serializer = adminSerializer.TermAndConditionsSerializer(terms, many=True)
            return {"data":serializer.data,"message":messages.TERMSANDCONDTIONS_FETCHED, "status":200}

        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG, "status":400}
    
    def update_terms_and_conditions(self, request, id):
        try:
            terms = TermAndConditionModel.objects.get(id=id)
            serializer = adminSerializer.TermAndConditionsSerializer(terms, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return {"data":serializer.data,"message":messages.TERMSANDCONDTIONS_UPDATE, "status":200}
            else:
                return {"data":None ,"message":messages.WENT_WRONG, "status":400}
        except Exception as e:
            return {"data":None, "message":messages.WENT_WRONG, "status":400}
# admin onboarding
    def admin_login(self, request):
        try:
                user = UserModel.objects.get(email=request.data["email"])
                if user.role != 3:
                    return {"data": None, "message": "You don't have access to login", "status": 403}
                if not check_password(request.data["password"], user.password):
                    return {"data": None, "message": messages.WRONG_PASSWORD, "status": 400}
        except UserModel.DoesNotExist:
                return {"data": None, "message": messages.EMAIL_NOT_FOUND, "status": 400}
        try:
            email = request.data["email"]
            password = request.data["password"]
            serializer = adminSerializer.ShowAdminDetialsByTokenSerializer(user)
            token = RefreshToken.for_user(user)
            
            all_obj = dict(serializer.data).copy()
            all_obj["access_token"] = str(token.access_token)
            all_obj["refresh_token"] = str(token)
            
            return {"data": all_obj, 'message': messages.LOGGED_IN, "status": 200}
        
        except Exception as e:
            return {"data": None, "message": str(e), "status": 400}
    

    def verify_otp(self, request):
        try:
            email = request.data["email"]
            otp = request.data["otp"]
            try:
                user = UserModel.objects.get(email=email)
                ENCODED_ID = user.encoded_id
            except UserModel.DoesNotExist:
                return {"data":None,"message":messages.EMAIL_NOT_FOUND,"status":400}
            if user.otp == otp:
                user.otp_email_verification = True
                if user.encoded_id == "":
                    ENCODED_ID = generate_encoded_id()
                    user.encoded_id = ENCODED_ID
                user.save()
                return {"data":{"encoded_id": ENCODED_ID}, "message":messages.OTP_VERIFIED,"status":200}
            else:
                return {"data":None,"message":messages.WRONG_OTP,"status":400}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

    def sent_otp(self, request):
        OTP = make_otp()
        email = request.data["email"]
        try:
            user = UserModel.objects.get(email=email)
            Thread(target=send_otp_via_mail, args=(email, )).start()
            user.otp = OTP
            user.save()
            return {"data":None,"message":messages.OTP_SENT_TO_MAIL,"status":200}
        except UserModel.DoesNotExist:
            return{"data":None,"message":messages.EMAIL_NOT_FOUND,"status":400}
    
    def forgot_password(self, request):
        encoded_id = request.data["encoded_id"]
        try:
            user = UserModel.objects.get(encoded_id=encoded_id)
            user.set_password(request.data["password"])
            user.save()
            return {"data":None,"message":messages.FORGOT_PASSWORD,"status":200}
        except UserModel.DoesNotExist:
            return {"data":None, "message":"Record not found", "status":400}
    
    def get_admin_details_by_token(self, request):
        try:
            user = UserModel.objects.get(id=request.user.id)
            serializer = adminSerializer.ShowAdminDetialsByTokenSerializer(user)
            return {"data":serializer.data,"message":messages.USER_DETAILS_FETCHED, "status":200}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG, "status":400}

    def update_admin_details_By_token(self, request):
        try:
            user = UserModel.objects.get(id=request.user.id)
            serializer = adminSerializer.updateAdminDetialsByTokenSerializer(user, data=request.data, context ={"profile_picture":request.data["profile_picture"]})
            if serializer.is_valid():
                serializer.save(profile_picture_id = request.data.get("profile_picture"))
                return {"data":serializer.data,"message":messages.UPDATE, "status":200}
            else:
                return{"data":None,"message":messages.WENT_WRONG, "status":400}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG, "status":400}

    
    def change_password_by_token(self, request):
        try:
            user = UserModel.objects.get(id = request.user.id)
            old_password = request.data["old_password"]
            new_password = request.data["new_password"]
            check_new_password = check_password(new_password,user.password)
            if check_new_password:
                return{"data":None,"message":messages.PASSWORD_NOT_SAME,"status":400}
            verify_password = check_password(old_password,user.password)
            if verify_password:
                user.set_password(new_password)
                user.save()
                return {"data":None,"message":messages.CHANGE_PASSWORD,"status":200}
            else:
                return {"data":None,"message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

    def logout(self, request):
        # token = request.META["HTTP_AUTHORIZATION"].split(" ")[1]
        # print(token, '-----')
        # token_obj = AccessToken(token)
        # BlacklistedToken(token=token_obj).save()
        # # token_obj.blacklist()
        # # jwt_token = JWTAuthentication().get_validated_token(request)
        # # AccessToken(token).blacklist()

        # return {"data": None, "message": messages.USER_LOGGED_OUT, "status": 200}
        # jwt_token = JWTAuthentication().get_validated_token(request)
        # token = str(jwt_token)
        # BlacklistedToken(token=token).save()
        return {"data": None, "message": messages.USER_LOGGED_OUT, "status": 200}
    
# manage customer module
    def add_new_customer(self, request):
        try:
            email = request.data["email"]
            data = UserModel.objects.filter(email=email)
            phone_no = request.data["phone_no"]
            phone_check = UserModel.objects.filter(phone_no=phone_no)
            if data:
                return {"data":None,"message":messages.EMAIL_EXISTS,"status":400}
            if phone_no:
                return {"data":None,"message":messages.PHONE_EXISTS,"status":400}
        except Exception as e:
            pass
        try:
            serializer = adminSerializer.AddNewClientByAdminSeriaizer(data = request.data)
            if serializer.is_valid():
                user = serializer.save(otp_email_verification=True, otp_phone_no_verification=True, profile_status=1, role=1)
                password = generate_password()
                user.set_password(password)
                send_password_via_mail(request.data["email"], password)
                user.save()
                address_location = request.data["address"]
                client_address = ManageAddressModel.objects.create(
                    address_location = request.data["address"],
                    user_id=user.id
                )
                client_address.save()
                return {"data": None, "data":serializer.data,"status":200}
            else:
                return {"data": serializer.errors, "message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}
    
    def get_custome_details_by_id(self, request, id):
        try:
            user = UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            return {"data": None,"message":messages.WENT_WRONG,"status":400}
        if user:
            serializer = adminSerializer.GetClientByAdminSeriaizer(user)
            return {"data":serializer.data,"message":messages.USER_DETAILS_FETCHED,"status":200}
        else:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}

    def edit_customer_by_admin(self,request,id):
        try:
            user = UserModel.objects.get(id = id)
        except UserModel.DoesNotExist:
            return {"data": None,"message":messages.WENT_WRONG,"status":400}
        if user:
            serializer = adminSerializer.AddNewClientByAdminSeriaizer(user, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return {"data":serializer.data,"message":messages.USER_DETAILS_FETCHED,"status":200}
            else:
                return {"data": serializer.errors, "message":messages.WENT_WRONG,"status":400}
        else:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}

    def delete_customer_by_admin(self, request, id):
        try:
            user= UserModel.objects.get(id=id)
        except UserModel.DoesNotExist:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}
        user.delete()
        return {"data": None, "message":messages.CUSTOMER_DELETE,"status":200}

    def get_all_customers(self, request):
        try:
            clients = UserModel.objects.filter(role=1).order_by('-id')
            pagination_obj = CustomPagination()
            search_keys = ["first_name__icontains", "email__icontains"]
            result = pagination_obj.custom_pagination(request, search_keys, \
                                                      adminSerializer.GetAllClientsDetailsSerializer, clients)
            # serializer = adminSerializer.GetAllClientsDetailsSerializer(clients, many=True)
            return {
                        "data":result["response_object"],
                        "total_records": result["total_records"],
                        "start": result["start"],
                        "length": result["length"], 
                        "message":messages.USER_DETAILS_FETCHED, 
                        "status":200
                    }
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}
        
    def bookings_of_customer(self, request, id):
        if request.data["key"] == 1:
            bookings = BookingTalentModel.objects.filter(client=id)
        elif request.data["key"] == 2:
            bookings = BookingTalentModel.objects.filter(client=id, status=2)
        elif request.data["key"] == 3:
            bookings = BookingTalentModel.objects.filter(client=id, status=1)
        elif request.data["key"] == 4:
            bookings = BookingTalentModel.objects.filter(client=id, status=4)
        elif request.data["key"] == 5:
            bookings = BookingTalentModel.objects.filter(client=id, status=3)
        pagination_obj = CustomPagination()
        search_keys = ["talent__email__icontains", "client__email__icontains"]
        result = pagination_obj.custom_pagination(request, search_keys, \
                                                    ShowBookingDetailsSerializer, bookings)
        data={}
        return {
                    "data":result["response_object"],
                    "total_records": result["total_records"],
                    "start": result["start"],
                    "length": result["length"], 
                    "message": "Customer bookings fetched successfully", 
                    "status":200
                }    


# manage categories

    def get_all_categories(self, request):
        try:
            categories = TalentCategoryModel.objects.all().order_by("-id")
            pagination_obj = CustomPagination()
            search_keys = ["name__icontains"]
            result = pagination_obj.custom_pagination(request, search_keys, \
                                                      adminSerializer.GetAllCategoriesSerializers, categories)
            return {
                        "data":result["response_object"],
                        "total_records": result["total_records"],
                        "start": result["start"],
                        "length": result["length"], 
                        "message": "Talent categories fetched successfully", 
                        "status":200
                    }
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}

    def all_category(self, request):
        try:
            category = TalentCategoryModel.objects.filter(is_active=True)
            serializer = adminSerializer.AllCategoriesSerializers(category, many =True)
            return {"data":serializer.data, "message":messages.FETCH,"status":200}
        except Exception as e:
            return {"data":None,"messges":messages.WENT_WRONG,"status":400}
    
    def get_categories_detail_by_id(self, request,id):
        try:
            category = TalentCategoryModel.objects.get(id=id)
            serializer  = adminSerializer.GetAllCategoriesSerializers(category)
            return {"data":serializer.data,"message":messages.CATEGORIES_LISTING,"status":200}
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}
    
    def update_category_by_id(self, request,id):
        try:
            category = TalentCategoryModel.objects.get(id=id)
            serializer = adminSerializer.CategorySerializer(category,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return {"data":serializer.data,"message":messages.UPDATE,"status":200}
            else:
                return {"data": None, "message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}

    def delete_category_by_id(self, request, id):
        try:
            category = TalentCategoryModel.objects.get(id=id)
            category.delete()
            return {"data": None, "message":messages.DELETE,"status":200}
        except Exception as e:
            return {"data": None, "message":messages.WENT_WRONG,"status":400}

    def get_all_subCategory(self, request):
        try:
            sub_category = TalentSubCategoryModel.objects.filter(category = request.data["category"])
            pagination_obj = CustomPagination()
            search_keys = ["name__icontains"]
            result = pagination_obj.custom_pagination(request, search_keys, \
                                                      adminSerializer.SubcategoryDetailsByCategoryIdSerializer, sub_category)
            return {
                        "data":result["response_object"],
                        "total_records": result["total_records"],
                        "start": result["start"],
                        "length": result["length"], 
                        "message": "Sub Categories fetched successfully", 
                        "status":200
                    }
        except Exception as e:
            return {"data": None, "message": str(e), "status": 400}

        
    def get_subcategory_by_id(self, request, id):
        try:
            subcategory = TalentSubCategoryModel.objects.get(id=id)
            serializer = adminSerializer.SubcategoryDetailsByCategoryIdSerializer(subcategory)
            if serializer.is_valid():
               return {"data":serializer.data,"message":messages.SUB_CATEGORIES_LISTING,"status":200}
            else:
                return {"data":None,"message":messages.WENT_WRONG,"status":400}
            
        except Exception as e:
            return {"data":serializer.data,"message":messages.SUB_CATEGORIES_LISTING,"status":400}
        
    def update_status_of_category(self, request, id):
        try:
            cat = TalentCategoryModel.objects.get(id=id)
            cat.is_active = request.data["is_active"]
            cat.save()
            return {"data": None, "message": "Status updated successfully", "status": 200}
        except TalentCategoryModel.DoesNotExist:    
            return {"data": None, "message": "Record not found", "status": 400}
        except Exception as err:    
            return {"data": None, "message": str(err), "status": 400}

    def update_status_of_sub_category(self, request, id):
        try:
            sub= TalentSubCategoryModel.objects.get(id=id)
            sub.is_active = request.data["is_active"]
            sub.save()
            return {"data": None, "message": "Status updated successfully", "status": 200}
        except TalentSubCategoryModel.DoesNotExist:    
            return {"data": None, "message": "Record not found", "status": 400}
        except Exception as err:    
            return {"data": None, "message": str(err), "status": 400}

    def update_subcategory_details(self, request, id):
        try:
            subcategory = TalentSubCategoryModel.objects.get(id=id)
            serializer = adminSerializer.SubcategoryDetailsByCategoryIdSerializer(subcategory,data = request.data)
            if serializer.is_valid():
                serializer.save()
                return {"data":serializer.data,"message":messages.UPDATE,"status":200}
            else:
                return {"data":None,"message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

    def delete_subcategory_by_id(self, request, id):
        try:
            sub_category = TalentSubCategoryModel.objects.get(id=id)
            sub_category.delete()
            return {"data":None,"message":messages.DELETE,"status":200}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}
            
            

# manage Artist

    def get_all_artist_Details(self, request):
        if request.data["verification_status"] == 0:
            users = UserModel.objects.filter(role=2, verification_status=0)
        elif request.data["verification_status"] == 1:
            users = UserModel.objects.filter(role=2, verification_status=1)
        elif request.data["verification_status"] == 2:
            users = UserModel.objects.filter(role=2, verification_status=2)
        users_id = [i.id for i in users]
        try:
            user = TalentDetailsModel.objects.filter(user__in=users_id).order_by('-id')
            pagination_obj = CustomPagination()
            search_keys = ["user__name__icontains", "user__email__icontains"]
            result = pagination_obj.custom_pagination(request, search_keys, \
                                                      adminSerializer.GetArtistDetailsSerializers, user)
            return {
                        "data":result["response_object"],
                        "total_records": result["total_records"],
                        "start": result["start"],
                        "length": result["length"], 
                        "message": "Artists fetched successfully", 
                        "status":200
                    }
            # serializer = adminSerializer.GetArtistDetailsSerializers(user,many = True)
            # return {"data":serializer.data,"messages":messages.USER_DETAILS_FETCHED,"status":200}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}
    

    def delete_artist_by_id(self, request, id):
        try:
            artist = UserModel.objects.get(id=id)
            artist.delete()
            return {"data":None,"message":messages.DELETE,"status":200}
        except Exception as e:
            return{"data":None,"message":messages.WENT_WRONG,"status":400}

    def get_artist_by_id(self, request, id):
        try:
            user_obj = UserModel.objects.get(id=id)
        except:
            return {"data":None,"messag":"User not found","status":400}
        try:
            user = TalentDetailsModel.objects.get(user_id=user_obj.id)
            serializer = adminSerializer.GetArtistDetailsByIdSerializer(user)
            return {"data":serializer.data,"messag":messages.USER_DETAILS_FETCHED,"status":200}
        except TalentDetailsModel.DoesNotExist:    
            user = TalentDetailsModel.objects.create(user_id=user_obj.id)
            serializer = adminSerializer.GetArtistDetailsByIdSerializer(user)
            return {"data":serializer.data,"messag":messages.USER_DETAILS_FETCHED,"status":200}
        except Exception as e:
            print(e)
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

    def Update_artist_details_by_id(self, request, id):
        data = {"user_details": {}, "extra_details": {}}
        data["user_details"]["first_name"] = request.data["first_name"]
        data["user_details"]["last_name"] = request.data["last_name"]
        data["user_details"]["email"] = request.data["email"]
        data["user_details"]["phone_no"] = request.data["phone_no"]
        data["user_details"]["date_of_birth"] = request.data["date_of_birth"]
        data["user_details"]["experience"] = request.data["experience"]
        data["user_details"]["gender"] = request.data["gender"]
        data["user_details"]["country_code"] = request.data["country_code"]
        data["user_details"]["address"] = request.data["address"]
        data["user_details"]["city"] = request.data["city"]
        data["user_details"]["state"] = request.data["state"]
        data["user_details"]["country"] = request.data["country"]
        data["user_details"]["profile_picture"] = request.data["profile_picture"]

        data["extra_details"]["bust"] = request.data["bust"]
        data["extra_details"]["waist"] = request.data["waist"]
        data["extra_details"]["hips"] = request.data["hips"]
        data["extra_details"]["height_feet"] = request.data["height_feet"]
        data["extra_details"]["height_inches"] = request.data["height_inches"]
        data["extra_details"]["weight"] = request.data["weight"]
        data["extra_details"]["hair_color"] = request.data["hair_color"] 
        data["extra_details"]["eye_color"] = request.data["eye_color"] 
        data["extra_details"]["booking_method"] = request.data["booking_method"]
        data["extra_details"]["portfolio"] = request.data["portfolio"]
        data["extra_details"]["cover_photo"] = request.data["cover_photo"]
        data["extra_details"]["categories"] = request.data["categories"]
        data["extra_details"]["sub_categories"] = request.data["sub_categories"]
        user_obj = UserModel.objects.get(id=id)
        user = adminSerializer.CreateUpdateTalentUserByAdminSerializer(user_obj, data=data["user_details"])
        NAME = request.data["first_name"] + " " + request.data["last_name"]
        if user.is_valid():
            user_obj = user.save(otp_email_verification=True, otp_phone_no_verification=True, \
                                 profile_status=1, role=2, name=NAME)
        model_obj = TalentDetailsModel.objects.get(user_id=user_obj.id)    
        model_details = adminSerializer.CreateModelStatusSerializer(model_obj, data=data["extra_details"])
        if model_details.is_valid():
            model_details.save(user_id=user_obj.id)
        return {"data":None, "message":"Artist updated successfully" ,"status":201}
    
    def bookings_of_artist(self, request, id):
        if request.data["key"] == 1:
            bookings = BookingTalentModel.objects.filter(talent=id)
        elif request.data["key"] == 2:
            bookings = BookingTalentModel.objects.filter(talent=id, status=2)
        elif request.data["key"] == 3:
            bookings = BookingTalentModel.objects.filter(talent=id, status=1)
        elif request.data["key"] == 4:
            bookings = BookingTalentModel.objects.filter(talent=id, status=4)
        elif request.data["key"] == 5:
            bookings = BookingTalentModel.objects.filter(talent=id, status=3)
        pagination_obj = CustomPagination()
        search_keys = ["talent__email__icontains", "client__email__icontains"]
        result = pagination_obj.custom_pagination(request, search_keys, \
                                                    ShowBookingDetailsSerializer, bookings)
        data ={}
        # data["Talent"]=result["response_objects"]
        return {
                    "data":result["response_object"],
                    "total_records": result["total_records"],
                    "start": result["start"],
                    "length": result["length"], 
                    "message": "Artist bookings fetched successfully", 
                    "status":200
                }

    def add_artist_through_admin(self, request):
        try:
            email = request.data["email"]
            data = UserModel.objects.filter(email=email)
            phone_no = request.data["phone_no"]
            phone_check = UserModel.objects.filter(phone_no=phone_no)
            if data:
                return {"data":None,"message":messages.EMAIL_EXISTS,"status":400}
            if phone_check:
                return {"data":None,"message":messages.PHONE_EXISTS,"status":400}
        except Exception as e:
            pass

        data = {"user_details": {}, "extra_details": {}}
        data["user_details"]["first_name"] = request.data["first_name"]
        data["user_details"]["last_name"] = request.data["last_name"]
        data["user_details"]["email"] = request.data["email"]
        data["user_details"]["phone_no"] = request.data["phone_no"]
        data["user_details"]["date_of_birth"] = request.data["date_of_birth"]
        data["user_details"]["experience"] = request.data["experience"]
        data["user_details"]["gender"] = request.data["gender"]
        data["user_details"]["country_code"] = request.data["country_code"]
        data["user_details"]["address"] = request.data["address"]
        data["user_details"]["city"] = request.data["city"]
        data["user_details"]["state"] = request.data["state"]
        data["user_details"]["country"] = request.data["country"]
        data["user_details"]["profile_picture"] = request.data["profile_picture"]

        data["extra_details"]["bust"] = request.data["bust"]
        data["extra_details"]["waist"] = request.data["waist"]
        data["extra_details"]["hips"] = request.data["hips"]
        data["extra_details"]["height_feet"] = request.data["height_feet"]
        data["extra_details"]["height_inches"] = request.data["height_inches"]
        data["extra_details"]["weight"] = request.data["weight"]
        data["extra_details"]["hair_color"] = request.data["hair_color"]
        data["extra_details"]["eye_color"] = request.data["eye_color"] 
        data["extra_details"]["booking_method"] = request.data["booking_method"]
        data["extra_details"]["portfolio"] = request.data["portfolio"]
        data["extra_details"]["cover_photo"] = request.data["cover_photo"]
        data["extra_details"]["categories"] = request.data["categories"]
        data["extra_details"]["sub_categories"] = request.data["sub_categories"]

        user = adminSerializer.CreateUpdateTalentUserByAdminSerializer(data=data["user_details"])
        NAME = request.data["first_name"] + " " + request.data["last_name"]
        if user.is_valid():
            user_obj = user.save(otp_email_verification=True, otp_phone_no_verification=True,\
                                 profile_status=1, role=2, name=NAME,verification_status=1)
            password = generate_password()
            user_obj.set_password(password)
            Thread(target=send_password_via_mail, args=(data["user_details"]["email"], password)).start()
            user_obj.save()
        else:
            return {"data":user.errors, "message":"Something went wrong while adding artist" ,"status":400}

        model_details = adminSerializer.CreateModelStatusSerializer(data=data["extra_details"])
        if model_details.is_valid():
            model_details.save(user_id=user_obj.id)
        else:
            return {"data":model_details.errors, "message":"Something went wrong while adding artist" ,"status":400}
        return {"data":None, "message":"Artist added successfully" ,"status":201}

    # def  booking_details_listing(self, request):
    #     try:
    #         print("came here")
    #         if not request.data.get("status"):
    #             book = BookingTalentModel.objects.all()
    #             serializer = adminSerializer.BookingDetailsModuleSerializer(book)
    #         # elif request.data["status"]:
    #         book = BookingTalentModel.objects.filter(status=request.data["status"])
    #         serializer = adminSerializer.BookingDetailsModuleSerializer(book)

    #         return {"data":serializer.data,"messag":messages.USER_DETAILS_FETCHED,"status":200}
    #     except Exception as e:
    #         print(e)
    #         return {"data":None,"message":messages.WENT_WRONG,"status":400}

    def add_sub_admin(self, request):
        try:
            data = request.data
            user_serializer = adminSerializer.CreateSubAdminSerializer(data=data)
            if user_serializer.is_valid():
                user_data = user_serializer.save(profile_status=1)
                password=generate_password()
                user_data.set_password(password)
                user_data.save()
                password = generate_password()
                user_data.set_password(password)
                send_password_via_mail(request.data["email"], password)
                user_data.save()
                for i in request.data['permissions']:
                    role_serializer = adminSerializer.CreateRolePermissionSubAdminSerializer(data=i)
                    if role_serializer.is_valid():
                        save_role_permission = role_serializer.save(user_id = user_serializer.data['id'])
                        save_role_permission.save()
                    else:
                        return {'data':role_serializer.errors, 'status':400}    
                return {'data':request.data, 'message': "Sub admin created",'status':201}
            return {'data':user_serializer.errors,"message": "Something went wrong",'status':400}
        except Exception as e:
            return {"error": str(e),"message":"Something went wrong", "status": 400}
        
    def update_sub_admin_by_id(self, request, id):
        user = UserModel.objects.filter(id = id).first()
        if not user:
            return {'data':None, "message":"User not found", 'status':400}
        try:
            data = {**request.data}
            role_permission_data = data.pop("permissions")
            user_serializer = adminSerializer.CreateSubAdminSerializer(user, data=data)
            if user_serializer.is_valid():
                user_data = user_serializer.save()
                for i in role_permission_data:
                    try:
                        get_permission = PermissionModel.objects.get(id = i["id"])
                        role_serializer = adminSerializer.CreateRolePermissionSubAdminSerializer(get_permission, data=i)
                    except:
                        role_serializer = adminSerializer.CreateRolePermissionSubAdminSerializer(data=i)
                    if role_serializer.is_valid():
                        save_role_permission = role_serializer.save(user_id = user.id)
                    else:
                        return {'data':role_serializer.errors, 'status':400}    
                return {'data':request.data, 'message': "Sub admin updated successfully",'status':201}
            return {'data':user_serializer.errors,"message":"Something went wrong",'status':400}
        except Exception as e:
            return {"error": str(e),"message":"Internal server error", "status": 500}



    def get_all_sub_admin(self, request):
        sub_obj = UserModel.objects.filter(role=4).order_by("created_at")
        pagination_obj = CustomPagination()
        search_keys = ["email__icontains"]
        result = pagination_obj.custom_pagination(request, search_keys, adminSerializer.GetSubAdminSerializer, sub_obj)
        return{'data': result,'message': "Sub admins fetched successfully", 'status': 200}
    

    def get_sub_admin_by_id(self,request, id):
        try:
            sub_obj = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return {"data":None,"message":"User not found", "status": 400}
        serializer = adminSerializer.GetSubAdminSerializer(sub_obj)
        return {"data": serializer.data,"message": "Sub admin details fetched successfully", "status": 200}

    def delete_sub_admin_by_id(self,request, id):
        try:
            sub_obj = UserModel.objects.get(pk=id)
        except UserModel.DoesNotExist:
            return {"data":None,"message":"User not found", "status": 400}
        sub_obj.delete()
        return {"data": None, "message": "Sub admin deleted successfully", "status": 200}

    # def edit_sub_admin_status_by_id(self,request, sub_admin_id):
    #     try:
    #         sub_obj = User.objects.get(pk=sub_admin_id)
    #     except User.DoesNotExist:
    #         return {"data":None,"message":get_message(request, 'NOT_FOUND'), "status": status.HTTP_404_NOT_FOUND}
    #     serializer = adminSerializer.GeteditSubAdminSerializer(sub_obj,request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return {"data": serializer.data,"message":get_message(request, 'FETCH'), "status": status.HTTP_200_OK}
    
    def change_status_of_customer_by_admin(self, request, id):
        try:
            customer = UserModel.objects.get(pk=id)
            customer.is_active = request.data["is_active"]
            customer.save()
            return {"data":None,"message": "status updated successfully", "status": 200}
        except UserModel.DoesNotExist:
            return {"data":None,"message": "User not found", "status": 400}

    def verify_artist(self, request, id):
        VERIFICATION_STATUS = request.data["verification_status"]
        try:
            user = UserModel.objects.get(id=id)
            user.verification_status = request.data["verification_status"]
            user.save()
            if VERIFICATION_STATUS == 1:
                var = "approved"
            else:
                var = "rejected"    
            return {"data":None, "message": f"Artist {var} successfully", "status": 200}
        except UserModel.DoesNotExist:
            return {"data":None,"message": "User not found", "status": 400}
        
    def all_bookings(self, request):
        if request.data["key"] == 1:
            bookings = BookingTalentModel.objects.all()
        elif request.data["key"] == 2:
            bookings = BookingTalentModel.objects.filter(status=2)
        elif request.data["key"] == 3:
            bookings = BookingTalentModel.objects.filter(status=1)
        elif request.data["key"] == 4:
            bookings = BookingTalentModel.objects.filter(status=4)
        elif request.data["key"] == 5:
            bookings = BookingTalentModel.objects.filter(status=3)
        pagination_obj = CustomPagination()
        search_keys = ["talent__email__icontains", "client__email__icontains", "client__first_name__icontains", \
                       "client__last_name__icontains","talent__first_name__icontains","talent__first_name__icontains",\
                       "talent__phone_no__icontains","client__phone_no__icontains"]
        result = pagination_obj.custom_pagination(request, search_keys, \
                                                    adminSerializer.BookingsSerializer, bookings)
        return {
                    "data":result["response_object"],
                    "total_records": result["total_records"],
                    "start": result["start"],
                    "length": result["length"], 
                    "message": "Artists fetched successfully", 
                    "status":200
                }
    
    def booking_details_by_id(self, request, id):
        try:
            booking = BookingTalentModel.objects.get(id=id)
        except BookingTalentModel.DoesNotExist:
            return {"data": None, "message": "Record not found", "status": 400}
        serializer = adminSerializer.BookingsSerializer(booking)
        return {"data": serializer.data, "message": "Booking details fetched successfully", "status": 200}

###### Dashboard Module


    def kpi(self, request):
        kpi_s ={}
        kpi_s["Total_customers"]=UserModel.objects.filter(role=1).count()
        kpi_s["Total_booking"]=BookingTalentModel.objects.all().count()
        kpi_s["Total_Artist"]=UserModel.objects.filter(role=2).count()
        return {"data":kpi_s,"message":messages.FETCH,"status":200}


    def client_chart(self, request):
        interval = request.data.get("interval")
        now = timezone.now()

        filtered_users = UserModel.objects.filter(role=1)
        
        def get_message(request, key):
            # Dummy function to simulate message retrieval
            return key

        if not interval:
            interval = "monthly"

        if interval == "daily":
            start_date = now - timezone.timedelta(days=now.weekday())  # Get the last Monday
            end_date = start_date + timezone.timedelta(days=6)  # Get the next Sunday
            delta = timezone.timedelta(days=1)
            date_counts = {day: 0 for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

            current_date = start_date
            while current_date <= end_date:
                count = filtered_users.filter(created_at__date=current_date).count()
                date_counts[current_date.strftime("%A")] = count  # Day of the week
                current_date += delta
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        elif interval == "weekly":
            current_year = now.year
            current_month = now.month
            start_date = timezone.datetime(current_year, current_month, 1).date()
            end_date = now.date()
            date_counts = {}
            
            # Calculate the number of weeks in the current month
            num_days_in_month = calendar.monthrange(current_year, current_month)[1]
            num_weeks = (num_days_in_month + start_date.weekday()) // 7 + 1

            for week_num in range(1, num_weeks + 1):
                date_counts[f"Week {week_num}"] = 0

            week_num = 1
            current_date = start_date
            while current_date <= end_date:
                week_start = current_date
                week_end = week_start + timezone.timedelta(days=6)
                count = filtered_users.filter(created_at__date__range=[week_start, week_end]).count()
                date_counts[f"Week {week_num}"] = count
                current_date = week_end + timezone.timedelta(days=1)
                week_num += 1
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())
            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)



        elif interval == "monthly":
            current_year = now.year
            start_date = timezone.datetime(current_year, 1, 1).date()
            end_date = now.date()
            date_counts = {month: 0 for month in calendar.month_name[1:]}

            current_date = start_date
            while current_date <= end_date:
                count = filtered_users.filter(created_at__year=current_year, created_at__month=current_date.month).count()
                date_counts[current_date.strftime("%B")] = count  # Month name
                current_date = (current_date.replace(day=28) + timezone.timedelta(days=4)).replace(day=1)
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        else:
            return {"data":None,'message': messages.WENT_WRONG, "status":400}
        
        return {"data":data, 'message': messages.FETCH,"status": 200}

    def artist_chart(self, request):
        interval = request.data.get("interval")
        now = timezone.now()

        filtered_users = UserModel.objects.filter(role=2)
        
        def get_message(request, key):
            # Dummy function to simulate message retrieval
            return key

        if not interval:
            interval = "monthly"

        if interval == "daily":
            start_date = now - timezone.timedelta(days=now.weekday())  # Get the last Monday
            end_date = start_date + timezone.timedelta(days=6)  # Get the next Sunday
            delta = timezone.timedelta(days=1)
            date_counts = {day: 0 for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

            current_date = start_date
            while current_date <= end_date:
                count = filtered_users.filter(created_at__date=current_date).count()
                date_counts[current_date.strftime("%A")] = count  # Day of the week
                current_date += delta
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        elif interval == "weekly":
            current_year = now.year
            current_month = now.month
            start_date = timezone.datetime(current_year, current_month, 1).date()
            end_date = now.date()
            date_counts = {}
            
            # Calculate the number of weeks in the current month
            num_days_in_month = calendar.monthrange(current_year, current_month)[1]
            num_weeks = (num_days_in_month + start_date.weekday()) // 7 + 1

            for week_num in range(1, num_weeks + 1):
                date_counts[f"Week {week_num}"] = 0

            week_num = 1
            current_date = start_date
            while current_date <= end_date:
                week_start = current_date
                week_end = week_start + timezone.timedelta(days=6)
                count = filtered_users.filter(created_at__date__range=[week_start, week_end]).count()
                date_counts[f"Week {week_num}"] = count
                current_date = week_end + timezone.timedelta(days=1)
                week_num += 1
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        elif interval == "monthly":
            current_year = now.year
            start_date = timezone.datetime(current_year, 1, 1).date()
            end_date = now.date()
            date_counts = {month: 0 for month in calendar.month_name[1:]}

            current_date = start_date
            while current_date <= end_date:
                count = filtered_users.filter(created_at__year=current_year, created_at__month=current_date.month).count()
                date_counts[current_date.strftime("%B")] = count  # Month name
                current_date = (current_date.replace(day=28) + timezone.timedelta(days=4)).replace(day=1)
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        else:
            return {"data":None,'message': messages.WENT_WRONG, "status":400}
        
        return {"data":data, 'message': messages.FETCH,"status": 200}

    def revenue_chart(self, request):
        pass

    def booking_chart(self, request):
        interval = request.data.get("interval")
        now = timezone.now()

        filtered_users = BookingTalentModel.objects.all()
        
        def get_message(request, key):
            # Dummy function to simulate message retrieval
            return key

        if not interval:
            interval = "monthly"

        if interval == "daily":
            start_date = now - timezone.timedelta(days=now.weekday())  # Get the last Monday
            end_date = start_date + timezone.timedelta(days=6)  # Get the next Sunday
            delta = timezone.timedelta(days=1)
            date_counts = {day: 0 for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]}

            current_date = start_date
            while current_date <= end_date:
                count = filtered_users.filter(created_at__date=current_date).count()
                date_counts[current_date.strftime("%A")] = count  # Day of the week
                current_date += delta
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        elif interval == "weekly":
            current_year = now.year
            current_month = now.month
            start_date = timezone.datetime(current_year, current_month, 1).date()
            end_date = now.date()
            date_counts = {}
            
            # Calculate the number of weeks in the current month
            num_days_in_month = calendar.monthrange(current_year, current_month)[1]
            num_weeks = (num_days_in_month + start_date.weekday()) // 7 + 1

            for week_num in range(1, num_weeks + 1):
                date_counts[f"Week {week_num}"] = 0

            week_num = 1
            current_date = start_date
            while current_date <= end_date:
                week_start = current_date
                week_end = week_start + timezone.timedelta(days=6)
                count = filtered_users.filter(created_at__date__range=[week_start, week_end]).count()
                date_counts[f"Week {week_num}"] = count
                current_date = week_end + timezone.timedelta(days=1)
                week_num += 1
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        elif interval == "monthly":
            current_year = now.year
            start_date = timezone.datetime(current_year, 1, 1).date()
            end_date = now.date()
            date_counts = {month: 0 for month in calendar.month_name[1:]}

            current_date = start_date
            while current_date <= end_date:
                count = filtered_users.filter(created_at__year=current_year, created_at__month=current_date.month).count()
                date_counts[current_date.strftime("%B")] = count  # Month name
                current_date = (current_date.replace(day=28) + timezone.timedelta(days=4)).replace(day=1)
            
            # Organize data into label and value arrays
            labels = list(date_counts.keys())
            values = list(date_counts.values())

            data = []
            for i in range(len(labels)):
                dict ={"labels":labels[i],"values":values[i]}
                data.append(dict)

        else:
            return {"data":None,'message': messages.WENT_WRONG, "status":400}
        
        return {"data":data, 'message': messages.FETCH,"status": 200}


################### Notifications module ################### 

    def add_notification(self, request):
        all_email_to_send, device_tokens = [], []
        try:
            if request.data["notification_for"] == 1:
                users = UserModel.objects.filter(role__in=[1,2])
            elif request.data["notification_for"] == 2:
                users = UserModel.objects.filter(role__in=[1])
            elif request.data["notification_for"] == 3:
                users = UserModel.objects.filter(role__in=[2])
            for i in users:
                all_email_to_send.append(i.email)
            if request.data["notification_type"] in (1,):
                send_notification_to_mail(all_email_to_send, request.data['notification_title'], request.data["notification_description"])   
            if request.data["notification_type"] in (2,):
                for i in device_tokens:
                    try:
                        push_service = FCMNotification(api_key=None)
                        result = push_service.notify_single_device(
                            registration_id=f"{i}",
                            message_title=request.data["notification_title"],
                            message_body=request.data["notification_description"],
                            )
                    except:
                        pass    
            NotificationModel.objects.create(
                title = request.data['notification_title'],
                description = request.data['notification_description'],
                notification_type = request.data['notification_type'],
                notification_for=request.data["notification_for"]
            )
            return {'data': None, 'message':"Notification sent successfully", 'status':200}    
        except Exception as e:
            return {'data':None, 'message':f"{e}", 'status':400}   

    def get_all_notification_listing(self, request):
        notification_obj = NotificationModel.objects.order_by("created_at")
        pagination_obj = CustomPagination()
        search_keys = ["title__icontains"]
        result = pagination_obj.custom_pagination(request, search_keys, \
                                                  adminSerializer.NotificationSerializer, notification_obj)
        return {
                        "data":result["response_object"],
                        "total_records": result["total_records"],
                        "start": result["start"],
                        "length": result["length"], 
                        "message": "All notifications fetched successfully", 
                        "status":200
                    }

    

## Manage CMs

    def add_privacy_poicy(self, request):
        try:
            privacy_policy = TermAndConditionModel.objects.filter(id=1)
            if not privacy_policy:
                serializer = adminSerializer.TermAndConditionsPPSerializer(data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"message":messages.ADD,"status":200}
                else:
                    return {"data":None,"message":messages.WENT_WRONG,"status":400}
            else:
                privacy_policy = TermAndConditionModel.objects.get(id=1)
                serializer = adminSerializer.TermAndConditionsPPSerializer(privacy_policy, data = request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"message":messages.ADD,"status":200}
                else:
                    return {"data":None,"message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

    def get_privacy_policy(self, request):
        try:
            pp = TermAndConditionModel.objects.all()
            serializer = adminSerializer.TermAndConditionsPPSerializer(pp,many= True)
            return {"data":serializer.data,"message":messages.FETCH,"status":200}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

    def add_customer_support(self, request):
        try:
            support_data = ContactUsModel.objects.filter(id=1)
            if not support_data:
                serializer = adminSerializer.CustomerSupportSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"message":messages.ADD,"status":200}
                else:
                    return {"data":None,"message":messages.WENT_WRONG,"status":400}
            else:
                support_data = ContactUsModel.objects.get(id=1)
                serializer = adminSerializer.CustomerSupportSerializer(support_data, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"message":messages.ADD,"status":200}
                else:
                    return {"data":None,"message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}


    def add_service_fees(self, request):
        try:
            support_data = ContactUsModel.objects.filter(id=1)
            if not support_data:
                serializer = adminSerializer.SetServiceFeesSserializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"message":messages.ADD,"status":200}
                else:
                    return {"data":None,"message":messages.WENT_WRONG,"status":400}
            else:
                support_data = ContactUsModel.objects.get(id=1)
                serializer = adminSerializer.SetServiceFeesSserializer(support_data, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return {"data":serializer.data,"message":messages.ADD,"status":200}
                else:
                    return {"data":None,"message":messages.WENT_WRONG,"status":400}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

    
    def get_service_fees(self, request):
        try:
            data = ContactUsModel.objects.get(id=1)
            serializer = adminSerializer.SetServiceFeesSserializer(data)
            return {"data":serializer.data,"message":messages.ADD,"status":200}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}


    def get_customer_support(self, request):
        try:
            data = ContactUsModel.objects.all()
            serializer = adminSerializer.CustomerSupportSerializer(data, many=True)
            return {"data":serializer.data,"message":messages.FETCH,"status":200}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}

######## Revenue Module ###############
    def get_all_revenue_details(self, request):
            data = BookingTalentModel.objects.all()
            pagination_obj = CustomPagination()
            search_keys = ["client__name__icontains","talent__name__icontains"]
            result = pagination_obj.custom_pagination(request, search_keys, \
                                                    adminSerializer.GetRevenueDetails, data)
            total_offer_price = BookingTalentModel.objects.aggregate(total_offer_price=Coalesce(Sum('offer_price'), Value(0)))
            total_count = BookingTalentModel.objects.count()
            total_revenue = total_offer_price['total_offer_price']
            return {
                            "data":result["response_object"],
                            "Total_revenue": total_revenue,
                            "total_records": result["total_records"],
                            "start": result["start"],
                            "length": result["length"], 
                            "message": messages.FETCH, 
                            "status":200
                        }

            


    ########### review module

    def get_all_review_details(self, request):
        data = ReviewAndRatingsModel.objects.all()
        pagination_obj = CustomPagination()
        search_keys = ["client__name__icontains","talent__name__icontains"]
        result = pagination_obj.custom_pagination(request, search_keys, \
                                                adminSerializer.GetAllRatingDetails, data)
        return {
                        "data":result["response_object"],
                        "total_records": result["total_records"],
                        "start": result["start"],
                        "length": result["length"], 
                        "message": messages.FETCH, 
                        "status":200
                    }

    ########## Colour Preferences #############

    def add_attribute_colour(self, request):
        ColourPreferencesModel.objects.create(
            name=request.data["name"],
            preference_type=request.data["type"]
        )
        return {"data": request.data, "message": "Attribute colour added successfully", "status": 201}

    def update_attribute_colour(self, request, id):
        try:
            obj = ColourPreferencesModel.objects.get(id=id)   
            obj.name = request.data["name"]
            obj.save()
            return {"data": request.data, "message": "Attribute colour updated successfully", "status": 200}
        except ColourPreferencesModel.DoesNotExist:
            return {"data": None, "message": "Record not found", "status": 400}
        except Exception as err:
            return {"data": str(err), "message": "Something went wrong", "status": 400}
    
    def delete_attribute_colour(self, request, id):
        try:
            obj = ColourPreferencesModel.objects.get(id=id)   
            obj.delete()
            return {"data": None, "message": "Attribute colour deleted successfully", "status": 200}
        except ColourPreferencesModel.DoesNotExist:
            return {"data": None, "message": "Record not found", "status": 400}
        except Exception as err:
            return {"data": str(err), "message": "Something went wrong", "status": 400}

    def all_attribute_colours(self, request):
        all_obj = ColourPreferencesModel.objects.filter(preference_type=request.data["type"]).values("id", "name", "preference_type", "is_active")
        for i in all_obj:
            i["type"] = i["preference_type"]  
        return {"data": all_obj, "message": "All hair colours fetched successfully", "status": 200}

