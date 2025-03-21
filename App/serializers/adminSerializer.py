from App.models.permissionModel import PermissionModel
from rest_framework import serializers
from App.models.talentCategoryModel import TalentCategoryModel
from App.models.talentSubCategoryModel import TalentSubCategoryModel
from App.models.faqModel import FAQModel
from App.models import TermAndConditionModel
from App.models import UserModel
from App.models.manageAddressModel import ManageAddressModel
from App.serializers.uploadMediaSerializer import CreateUpdateUploadMediaSerializer
from App.models.talentDetailsModel import TalentDetailsModel
from App.models.uploadMediaModel import UploadMediaModel
from App.models.bookingTalentModel import BookingTalentModel
# from artist_python_backend.App.models import manageAddressModel
from App.serializers.Clientserializer import TalentBasicDetails
from App.models.contactUsModel import ContactUsModel
from App.models.notificationModel import NotificationModel
from App.models.ratingsModel import ReviewAndRatingsModel
from App.utils.choiceFields import MODULE_PATHS
import uuid

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentCategoryModel
        fields = ["id", "name","image"]

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentSubCategoryModel
        fields = ["id", "name", "category"]


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQModel
        fields = ["id","question","answer"]

class TermAndConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermAndConditionModel
        fields = ["id", "data"]

class TermAndConditionsPPSerializer(serializers.ModelSerializer):
    class Meta:
        model = TermAndConditionModel
        fields = ["id", "privacy_policy"]


class AdminVerifyOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id","email","otp","otp_email_verification"]

class AddNewClientByAdminSeriaizer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ["id","email","first_name","last_name","phone_no","address","city","state","country", \
                  "profile_picture", "country_code"]

class GetClientByAdminSeriaizer(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = UserModel
        fields = ["id","email","first_name","last_name","phone_no","address","city","state","country", \
                  "profile_picture", "country_code"]


class ManageAddressByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageAddressModel
        fields = ["id","address_location","user"]

class GetAllClientsDetailsSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = UserModel
        fields = ["id", "full_name", "email", "country_code", "phone_no", "address", "is_active", \
                  "profile_picture", "city", "state", "country"]

    def get_full_name(self, obj):
        try:
            fullname=obj.first_name +" "+ obj.last_name
            return fullname
        except:
            return None    


class ShowAdminDetialsByTokenSerializer(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    permissions = serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ["id","username","country_code","email","phone_no", "role", "address","profile_picture", "permissions"]
    def get_permissions(self, obj):
        try:
            permissions = PermissionModel.objects.filter(user=obj.id)
            serializer = GetRolePermissionSubAdminSerializer(permissions, many=True)
            return serializer.data
        except:
            return None    

    def get_address(self, obj):
        try:
            address = ManageAddressModel.objects.filter(user_id=obj).first
            serializer = ManageAddressByAdminSerializer(address, many=True)
            return serializer.data
        except Exception as e:
            return None

class updateAdminDetialsByTokenSerializer(serializers.ModelSerializer):
    profile_picture =serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ["id","username","country_code","email","phone_no","address","profile_picture"]
    
    def get_profile_picture(self, obj):
        try:
            get_profile_picture = UploadMediaModel.objects.get(id = self.context.get("profile_picture"))
            serializers = CreateUpdateUploadMediaSerializer(get_profile_picture)
            return serializers.data
        except Exception as e:
            return obj.profile_picture_id

class GetAllCategoriesSerializers(serializers.ModelSerializer):
    image = CreateUpdateUploadMediaSerializer()
    update_at = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()
    class Meta:
        model = TalentCategoryModel
        fields = ["id", "name", "update_at", "is_active", "key","image"]

    def get_update_at(self, obj):
       return obj.updated_at.date()
    def get_key(self, obj):
        if (obj.name).lower() in ["actor", "model"]:
            return (obj.name).lower()
        else:
            return None

class AllCategoriesSerializers(serializers.ModelSerializer):
    update_at = serializers.SerializerMethodField()
    key = serializers.SerializerMethodField()
    class Meta:
        model = TalentCategoryModel
        fields = ["id", "name", "update_at", "is_active", "key"]

    def get_update_at(self, obj):
       return obj.updated_at.date()
    def get_key(self, obj):
        if (obj.name).lower() in ["actor", "model"]:
            return (obj.name).lower()
        else:
            return None

class SubcategoryDetailsByCategoryIdSerializer(serializers.ModelSerializer):
    update_at  = serializers.SerializerMethodField()

    class Meta:
        model = TalentSubCategoryModel
        fields = ["id","name","update_at","is_active"]

    def get_update_at(self, obj):
        return obj.updated_at.date()

#manage artist serializers


class GetArtistDetailsSerializers(serializers.ModelSerializer):
    id = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    country_code = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone_no = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    sub_categories = serializers.SerializerMethodField()
    date_of_birth = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()
    verification_status = serializers.SerializerMethodField()
    is_active = serializers.SerializerMethodField()

    class Meta:
        model = TalentDetailsModel
        fields = ["id","name","email","profile_picture","gender","country_code","phone_no","date_of_birth",\
                  "experience","booking_method","address","categories","sub_categories", "is_active", "verification_status"]

    def get_date_of_birth(self, obj):
        return obj.user.date_of_birth
    def get_is_active(self, obj):
        return obj.user.is_active
    def get_id(self, obj):
        # print(obj)
        return obj.user.id

    def get_experience(self, obj):
        return obj.user.experience
    def get_profile_picture(self, obj):
        p_obj = obj.user.profile_picture
        serializers= CreateUpdateUploadMediaSerializer(p_obj)
        return serializers.data
    def get_name(self, obj):
        return obj.user.first_name+" "+obj.user.last_name
    def get_address(self, obj):
        return obj.user.address
    def get_email(self, obj):
        return obj.user.email
    def get_phone_no(self, obj):
        return obj.user.phone_no
    def get_country_code(self, obj):
        return obj.user.country_code
    def get_gender(self, obj):
        try:
            return obj.user.get_gender_display()
        except:    
            return obj.user.gender
    def get_categories(self, obj):
        try:
            categories = TalentCategoryModel.objects.filter(id__in=obj.categories)
            cat_serializer = CategorySerializer(categories, many=True)
            return cat_serializer.data
        except:
            return obj.categories
    def get_sub_categories(self, obj):
        try:
            sub_categories = TalentSubCategoryModel.objects.select_related("category").filter(id__in=obj.sub_categories)
            sub_cat_serializer = SubCategorySerializer(sub_categories, many=True)
            return sub_cat_serializer.data
        except:
            return obj.sub_categories
    def get_verification_status(self, obj):
        try:
            return obj.user.get_verification_status_display()
        except:
            return obj.user.verification_status

class GetArtistDetailsByIdSerializer(serializers.ModelSerializer):
    country_code = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()
    state = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    phone_no = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    sub_categories = serializers.SerializerMethodField()
    date_of_birth = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    profile_picture = serializers.SerializerMethodField()
    cover_photo = CreateUpdateUploadMediaSerializer()
    portfolio = serializers.SerializerMethodField()
    booking_method = serializers.SerializerMethodField()
    hair_color = serializers.SerializerMethodField()
    eye_color = serializers.SerializerMethodField()
    weight =serializers.SerializerMethodField()

    class Meta:
        model = TalentDetailsModel
        fields = ["id", "first_name", "last_name", "name","email","profile_picture","gender","state","city","country","country_code",\
                  "phone_no","date_of_birth","experience",'booking_method',"address", "categories","sub_categories",\
                  "bust","waist","hips","height_feet","height_inches","weight","hair_color","eye_color","portfolio",\
                  "cover_photo"]

    def get_weight(self, obj):
        if obj.weight is not None:
            return round(float(obj.weight),2)
        else:
            return obj.weight

    def get_date_of_birth(self, obj):
        return obj.user.date_of_birth
    def get_hair_color(self, obj):
        try:
            return obj.hair_color_id
        except:
            return None
    def get_eye_color(self, obj):
        try:
            return obj.eye_color_id
        except:
            return None
    def get_experience(self, obj):
        return obj.user.experience
    def get_profile_picture(self, obj):
        p_obj = obj.user.profile_picture
        serializers= CreateUpdateUploadMediaSerializer(p_obj)
        return serializers.data
    def get_country(self, obj):
        return obj.user.country
    def get_booking_method(self, obj):
        return obj.booking_method
    def get_city(self, obj):
        return obj.user.city
    def get_state(self, obj):
        return obj.user.state
    def get_cover_photo(self,obj):
        image= obj.cover_photo
        serializer = CreateUpdateUploadMediaSerializer(image)
        return serializer.data
    def get_name(self, obj):
        return obj.user.name
    def get_first_name(self, obj):
        return obj.user.first_name
    def get_last_name(self, obj):
        return obj.user.last_name
    def get_address(self, obj):
        return obj.user.address
    def get_email(self, obj):
        return obj.user.email
    def get_phone_no(self, obj):
        return obj.user.phone_no
    def get_country_code(self, obj):
        return obj.user.country_code
    def get_gender(self, obj):
        return obj.user.gender
    def get_categories(self, obj):
        try:
            categories = TalentCategoryModel.objects.filter(id__in=obj.categories)
            cat_serializer = AllCategoriesSerializers(categories, many=True)
            return cat_serializer.data
        except:
            return obj.categories
    def get_sub_categories(self, obj):
        try:
            sub_categories = TalentSubCategoryModel.objects.select_related("category").filter(id__in=obj.sub_categories)
            sub_cat_serializer = SubCategorySerializer(sub_categories, many=True)
            return sub_cat_serializer.data
        except:
            return obj.sub_categories
    # def get_portfolio(self, obj):
    #     try:
    #         media = UploadMediaModel.objects.filter(id=obj.portfolio[0]).first()
    #         if media:
    #             serializer = CreateUpdateUploadMediaSerializer(media)
    #             return serializer.data
    #     except:
    #         return obj.portfolio

    def get_portfolio(self, obj):
        try:
            l = []
            for i in obj.portfolio:
                media = UploadMediaModel.objects.get(id=i)
                if media:
                    serializer = CreateUpdateUploadMediaSerializer(media)
                    l.append(serializer.data)
            return l 
        except:
            return obj.portfolio

# class bookingClientArtistDetailsSerializer(serializers.ModelSerializer):
#     profile_picture = CreateUpdateUploadMediaSerializer()
#     full_name = serializers.SerializerMethodField()
#     class Meta:
#         model = UserModel
#         fields = ["id","full_name","profile_picture"]

#     def get_full_name(self, obj):
#         return obj.first_name+" "+obj.last_name

# class ManageAddressBookingDetailsModule(serializers.ModelSerializer):
#     class Meta:
#         model = ManageAddressModel
#         fields = "__all__"

# #booking Module
# class BookingDetailsModuleSerializer(serializers.ModelSerializer):
#     client = serializers.SerializerMethodField()
#     artist = serializers.SerializerMethodField()
#     address = serializers.SerializerMethodField()
#     profession= serializers.SerializerMethodField()   # category
#     description = serializers.SerializerMethodField()
#     service_fee = serializers.SerializerMethodField()
#     service = serializers.SerializerMethodField()   # sub-category
#     class Meta:
#         model = BookingTalentModel
#         fields = ["id","client","artist","profession","address","description","date","time","duration","offer_price","service_fee","service","status","currency"]

#     def get_client(self, obj):
#         id=obj.first().client.id
#         # id = obj.client
#         user = UserModel.objects.get(id =id)
#         serializer = bookingClientArtistDetailsSerializer(user)
#         print(serializer.data,"44444444444444444444")
#         return serializer.data
    
#     def get_artist(self, obj):
#         print(obj.first().talent.id,"2222222222")
#         id = obj.first().talent.id
#         user = UserModel.objects.get(id =id)
#         serializer = bookingClientArtistDetailsSerializer(user)
#         print(serializer.data,"4444444444444444444455555555555555")
#         return serializer.data

#     def get_address(self, obj):
#         id = obj.address
#         address = ManageAddressModel.objects.get(id=id)
#         serializer = ManageAddressBookingDetailsModule(address)
#         return serializer.data

#     def get_profession(self, obj):
#         id = obj.artist
#         category =TalentDetailsModel.objects.get(user_id=id).categories
#         serializer = CategorySerializer(category, many=True)
#         return serializer.data

#     def get_service(self, obj):
#         id = obj.artist
#         sub_categories = TalentDetailsModel.objects.get(user_id=id).sub_categories
#         serializers = SubCategorySerializer(sub_categories, many = True)
#         return serializers.data

#     def get_service_fee(self, obj):
#         service = 15
#         return service
    
#     def get_description(self, obj):
#         return obj.comment
        

        



        

class CreateUpdateTalentUserByAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ("id", "profile_picture", "first_name", "last_name", "email", "gender", "country_code", "phone_no",\
                  "date_of_birth", "experience", "address", "city", "state", "country")
        
class CreateModelStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentDetailsModel
        fields = ('id', 'bust', 'waist', 'hips', 'height_feet', 'height_inches', 'weight', 'hair_color',\
                   'eye_color',"booking_method" ,'portfolio', 'cover_photo', 'categories', 'sub_categories',\
                    'services')        
        
class CreateRolePermissionSubAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PermissionModel
        fields = ['id','module', 'is_add', 'is_view', 'is_edit', 'is_delete']

class GetRolePermissionSubAdminSerializer(serializers.ModelSerializer):
    module_path = serializers.SerializerMethodField()
    module_label = serializers.SerializerMethodField()
    class Meta:
        model = PermissionModel
        fields = ['id','module', 'module_label', 'is_add', 'is_view', 'is_edit', 'is_delete', 'module_path']
    def get_module_label(self, obj):
        try:
            return obj.get_module_display()
        except:
            return obj.module
    def get_module_path(self, obj):
        try:
            return MODULE_PATHS[obj.module]
        except:
            return None

class GetSubAdminSerializer(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    permissions = serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ["id","name", "email", "country_code", "phone_no","profile_picture", "permissions"]
    def get_permissions(self, obj):
        try:
            p = PermissionModel.objects.filter(user=obj.id)
            serializer = GetRolePermissionSubAdminSerializer(p, many=True)
            return serializer.data
        except:
            return None

class CreateSubAdminSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserModel
        fields = ("id","name","email","country_code","phone_no","profile_picture",'role')
        extra_kwargs = {'role': {'default': 4}}

class BookingsSerializer(serializers.ModelSerializer):
    talent = TalentBasicDetails()
    client = TalentBasicDetails()
    address = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    # booking_id = serializers.SerializerMethodField()
    class Meta:
        model = BookingTalentModel
        fields = ["id", "talent", "client", "address", "date", "time", "duration", "offer_price", "comment",\
                   "currency", "status"]

    # def get_booking_id(self, obj):
    #     return str(uuid.uuid4())

    def get_address(self, obj):
        try:
            return obj.client.address
        except Exception as e:
            return None    
    def get_status(self, obj):
        try:
            return obj.get_status_display()
        except Exception as e:
            return obj.status

class ArtistBookingsAdminSerializer(serializers.ModelSerializer):
    customer_name = serializers.SerializerMethodField()
    artist_name = serializers.SerializerMethodField()
    profession = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()
    service = serializers.SerializerMethodField()
    service_fee = serializers.SerializerMethodField()
    class Meta:
        model = BookingTalentModel
        fields = ["id", "customer_name", "artist_name", "profession", "date", "time", "duration", \
                  "service", "status", "service_fee", "offer_price"]
    def get_customer_name(self, obj):
        try:
            return obj.client.name
        except:
            return obj.client
    def get_artist_name(self, obj):
        try:
            return obj.talent.name
        except:
            return obj.talent
    def get_profession(self, obj):
        try:
            talent_details = TalentDetailsModel.objects.get(user_id=obj.talent_id)
            cat = talent_details.categories
            cat_names = ", ".join([i[0] for i in TalentCategoryModel.objects.filter(id__in=cat).values_list("name")])
            return cat_names
        except Exception as err:
            return ""
    def get_status(self, obj):
        try:
            return obj.get_status_display()
        except:
            return obj.status
    def get_service(self, obj):
        try:
            service = ""
            for i in obj.services:
                service += ", " + i["service"]
            return service
        except:
            return ""    
    def get_service_fee(self, obj):
        try:
            service_fee = 0
            for i in obj.services:
                service_fee += i["price"]
            return service_fee
        except:
            return None

### Revenue Module serializers

class clientTalentDetailsSerializer(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = UserModel
        fields = ["id","profile_picture","first_name","last_name","name","phone_no","country_code","email"]


class GetRevenueDetails(serializers.ModelSerializer):
    client = clientTalentDetailsSerializer()
    talent = clientTalentDetailsSerializer()
    booking = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    class Meta:
        model = BookingTalentModel
        fields = ["id","client","talent","services","currency","price","booking"]

    def get_booking(self, obj):
        try:
            return obj.get_status_display()
        except:
            return obj.status
    
    def get_price(self, obj):
        return obj.offer_price


##customerSupport serializers

class CustomerSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model= ContactUsModel
        fields = ["id","name","country_code","phone_no","data","privacy_policy"]

class SetServiceFeesSserializer(serializers.ModelSerializer):
    class Meta:
        model =ContactUsModel
        fields = ["service_price"]


###notification serializer

class NotificationSerializer(serializers.ModelSerializer):
    notification_type = serializers.SerializerMethodField()
    notification_for = serializers.SerializerMethodField()
    date = serializers.SerializerMethodField()
    class Meta:
        model = NotificationModel
        fields = ["id", "title", "description", "notification_type", "notification_for", "date"]
    def get_notification_type(self, obj):
        return obj.get_notification_type_display()
    def get_notification_for(self, obj):
        return obj.get_notification_for_display()
    def get_date(self, obj):
        return str(obj.created_at.date())

##### rating and review serializer

class clientRatingSerializer(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = UserModel
        fields = ["id","name","profile_picture","phone_no","country_code"]

class GetAllRatingDetails(serializers.ModelSerializer):
    client = clientRatingSerializer()
    talent = clientRatingSerializer()
    class Meta:
        model = ReviewAndRatingsModel
        fields = ["id","client","talent","rating","review","best_liked", "created_at"]
