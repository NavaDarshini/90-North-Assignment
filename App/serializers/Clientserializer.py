from datetime import datetime, timedelta
from rest_framework import serializers
from App.models.userModel import UserModel
from App.models.manageAddressModel import ManageAddressModel
from App.models.talentSubCategoryModel import TalentSubCategoryModel
from App.models.talentCategoryModel import TalentCategoryModel
from App.models.talentDetailsModel import TalentDetailsModel
from App.serializers.uploadMediaSerializer import CreateUpdateUploadMediaSerializer
from App.models.uploadMediaModel import UploadMediaModel
from App.models.bookingTalentModel import BookingTalentModel
from App.utils.sendOtp import generate_access_token
from App.models.ratingsModel import ReviewAndRatingsModel
from django.db.models import Avg
from datetime import date
from App.models.contactUsModel import ContactUsModel
from App.models.appNotificationModel import AppNotificationModel
from App.serializers.ratingsSerializer import GetRatingSerializer

class CreateClientSerializers(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ("id", "profile_picture", "first_name", "email", "last_name", "gender", "country_code", "phone_no",\
                  "date_of_birth", "experience", "address", "city", "state", "country", "encoded_id","token","otp_email_verification","otp_phone_no_verification")
    def get_token(self, obj):
        token = generate_access_token(obj)
        return token 

class GetClientDetails(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = UserModel
        fields = ("id", "profile_picture", "first_name", "email", "last_name", "name", "gender", "country_code", "phone_no",\
                  "date_of_birth", "experience", "address", "city", "state", "country", "encoded_id","otp_email_verification","otp_phone_no_verification")
class GetUserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = UserModel
        fields = ["id", "profile_picture", "first_name", "email", "last_name", "gender", "country_code", "phone_no",\
                  "date_of_birth", "experience", "address", "city", "state", "country", "otp_email_verification",\
                  "otp_phone_no_verification", "profile_status","encoded_id", "token"]
    def get_token(self, obj):
        if self.context.get("give_token"):
            token = generate_access_token(obj)
            return token
        else:
            return ""


class AddAddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManageAddressModel
        fields = ["id","address_location", "house_flat_block_no", "landmark", "street_no", "phone_no_manage_address", "address_type","city","state","country"]
class SubCategories(serializers.ModelSerializer):
    class Meta:
        model = TalentSubCategoryModel
        fields =["id", "name"]

class TalentBasedOnSubcategories(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = TalentDetailsModel
        fields = fields = ('id', 'bust', 'waist', 'hips', 'height_feet', 'height_inches', 'weight', 'hair_color', 'eye_color', 'booking_method')

class TalentCategoryListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TalentCategoryModel
        fields = ["id", "name"]

class TalentDetailsBasedOnSubcategories(serializers.ModelSerializer):
    hair_color = serializers.SerializerMethodField()
    eye_color = serializers.SerializerMethodField()
    booking_method = serializers.SerializerMethodField()
    portfolio = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    sub_categories = serializers.SerializerMethodField()
    cover_photo = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = TalentDetailsModel
        fields =["id","bust","waist","hips","height_feet","height_inches","weight","hair_color","eye_color",\
                 "booking_method","portfolio","cover_photo", "categories", "sub_categories"]
    def get_hair_color(self, obj):
        try:
            return obj.hair_color.name
        except:
            return obj.hair_color_id
    def get_eye_color(self, obj):
        try:
            return obj.eye_color.name
        except:
            return obj.eye_color_id
    def get_booking_method(self, obj):
        try:
            data = []
            for i in obj.booking_method:
                if i == 1:
                    data.append("PRE BOOK")
                elif i == 2:
                    data.append("PAY LATER")
            return data            
        except:
            return obj.booking_method
    def get_portfolio(self, obj):
        data = []
        try:
            for i in obj.portfolio:
                media = UploadMediaModel.objects.filter(id=i).first()
                if media:
                    data.append(CreateUpdateUploadMediaSerializer(media).data)
                else:
                    pass
            return data        
        except:
            return obj.portfolio
    def get_categories(self, obj):
        cat = TalentCategoryModel.objects.filter(id__in=obj.categories)
        serializer = TalentCategoryListingSerializer(cat, many=True)
        return serializer.data 
    def get_sub_categories(self, obj):
        sub_categories = TalentSubCategoryModel.objects.filter(id__in=obj.sub_categories)
        serializer = SubCategories(sub_categories, many=True)
        return serializer.data 


class TalentListingDetailsSerializer(serializers.ModelSerializer):
    sub_categories = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    profile_picture = CreateUpdateUploadMediaSerializer()
    class Meta:
        model = UserModel
        fields = ["id", "first_name","last_name", "profile_picture", "email",
                  "name", "address",\
                  "rating", "profile_status", "sub_categories", "categories"]
    def get_sub_categories(self, obj):
        details = TalentDetailsModel.objects.filter(user=obj.id).first()
        if details:
            sub_categories = TalentSubCategoryModel.objects.filter(id__in=details.sub_categories)
            serializer = SubCategories(sub_categories, many=True)
            return ", ".join([i["name"] for i in serializer.data])
        else:
            return []    
    def get_categories(self, obj):
        details = TalentDetailsModel.objects.filter(user=obj.id).first()
        if details:
            categories = TalentSubCategoryModel.objects.filter(id__in=details.categories)
            serializer = TalentCategoryListingSerializer(categories, many=True)
            return serializer.data
        else:
            return []    
    def get_rating(self, obj):
        try:
            return obj.average_rating
        except:
            return None

class TalentDetailsBasedOnIOSOtherDetailsSubcategories(serializers.ModelSerializer):
    booking_method = serializers.SerializerMethodField()
    portfolio = serializers.SerializerMethodField()
    categories = serializers.SerializerMethodField()
    sub_categories = serializers.SerializerMethodField()
    cover_photo = CreateUpdateUploadMediaSerializer()
    

    class Meta:
        model = TalentDetailsModel
        fields = ["booking_method","portfolio","cover_photo", "categories", "sub_categories"]
    def get_booking_method(self, obj):
        try:
            return obj.get_booking_method_display()
        except:
            return obj.booking_method
    def get_portfolio(self, obj):
        data = []
        try:
            for i in obj.portfolio:
                media = UploadMediaModel.objects.filter(id=i).first()
                if media:
                    data.append(CreateUpdateUploadMediaSerializer(media).data)
                else:
                    pass
            return data        
        except:
            return obj.portfolio
    def get_categories(self, obj):
        cat = TalentCategoryModel.objects.filter(id__in=obj.categories)
        serializer = TalentCategoryListingSerializer(cat, many=True)
        return serializer.data 
    def get_sub_categories(self, obj):
        sub_categories = TalentSubCategoryModel.objects.filter(id__in=obj.sub_categories)
        serializer = SubCategories(sub_categories, many=True)
        return serializer.data 

   




class TalentDetailsBasedOnIOSSubcategories(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()
    hair_color = serializers.SerializerMethodField()
    eye_color = serializers.SerializerMethodField()
    height = serializers.SerializerMethodField()
    
    class Meta:
        model = TalentDetailsModel
        fields =["gender","age","city","hair_color","eye_color","height","weight","bust","waist","hips"]
    def get_hair_color(self, obj):
        try:
            return obj.hair_color.name
        except:
            return obj.hair_color_id

    def get_height(self,obj):
        return str(obj.height_feet)+"'"+str(obj.height_inches)
    def get_gender(self, obj):
        try:
            return obj.user.get_gender_display()
        except:
            return obj.user.gender
    def get_age(self, obj):
        current_date =  date.today()
        user_date=obj.user.date_of_birth
        age = (current_date-user_date).days
        age = age/365.25
        return int(age)

    def get_city(self, obj):
        return obj.user.city

    def get_eye_color(self, obj):
        try:
            return obj.eye_color.name
        except:
            return obj.eye_color_id
    

class TalentBasicDetailsIOS(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    professional_details = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    number_of_ratings = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ["id", "first_name","last_name","profile_picture", "email", "experience","phone_no",\
                  "country_code","country", "name", "address",\
                  "state", "profile_status", "professional_details", "services", "average_rating", "number_of_ratings", "ratings"]
    def get_professional_details(self, obj):
        details = TalentDetailsModel.objects.filter(user=obj.id).first()
        if details:
            serializer = TalentDetailsBasedOnIOSOtherDetailsSubcategories(details)
            return serializer.data
        else:
            return {}    
    def get_services(self, obj):
        details = TalentDetailsModel.objects.filter(user=obj.id).first()
        if details:
            for service in details.services:
                service['price'] = float(f"{float(service['price']):.2f}")
            return details.services
        else:
            return []
    def get_number_of_ratings(self, obj):
        try:
            count_of_ratings = ReviewAndRatingsModel.objects.filter(talent=obj.id).count()
            return count_of_ratings
        except:
            return 0    
    def get_ratings(self, obj):
        try:
            ratings = ReviewAndRatingsModel.objects.filter(talent=obj.id)
            checking_date = datetime.now()-timedelta(days=7)
            ratings = ratings.exclude(created_at__lt=checking_date).order_by("-id")
            serializer = GetRatingSerializer(ratings, many=True)
            return serializer.data[:10]
        except:
            return []


class TalentBasicDetails(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    professional_details = serializers.SerializerMethodField()
    services = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ["id", "first_name","last_name","profile_picture", "email", "gender", "experience","phone_no",\
                  "country_code", "city","country", "name", "address", "tags",\
                  "state", "profile_status", "professional_details", "services", "average_rating"]
    def get_professional_details(self, obj):
        details = TalentDetailsModel.objects.filter(user=obj.id).first()
        if details:
            serializer = TalentDetailsBasedOnSubcategories(details)
            return serializer.data
        else:
            return {}    
    def get_tags(self, obj):
        user_obj = TalentDetailsModel.objects.filter(user=obj.id).first()
        if user_obj:
            return user_obj.tags
        else:
            return None    
    def get_gender(self, obj):
        try:
            return obj.get_gender_display()
        except:
            return obj.gender
    def get_services(self, obj):
        details = TalentDetailsModel.objects.filter(user=obj.id).first()
        if details:
            return details.services
        else:
            return []


class BookingProposalSerializers(serializers.ModelSerializer):
    pass




class BookingDetailsSerializer(serializers.ModelSerializer):
    client = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = BookingTalentModel
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    profile_picture = CreateUpdateUploadMediaSerializer()
    rating = serializers.SerializerMethodField()
    class Meta:
        model = UserModel
        fields = ["id", "first_name", "last_name", "name", "profile_picture", "rating"]
    def get_rating(self, obj):
        try:
            if obj.role == 2:
                avg_ratings = ReviewAndRatingsModel.objects.filter(talent=obj.id).aggregate(Avg("rating"))
                return avg_ratings["rating__avg"]
            return None    
        except Exception as err:
            return None

class ShowBookingDetailsSerializer(serializers.ModelSerializer):
    talent = UserSerializer()
    client = UserSerializer()
    subcategories = serializers.SerializerMethodField()
    address = AddAddressDetailsSerializer()
    status = serializers.SerializerMethodField()
    track_booking = serializers.SerializerMethodField()
    service_price = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()
    class Meta:
        model = BookingTalentModel
        fields = ["id", "talent", "client", "subcategories", "address", "date", "time", "duration", \
                  "status", "track_booking", "offer_price", "counter_offer_price", "final_price", "comment", \
                  "services", "service_price", "rating_by_client", "rating_by_talent", "client_marked_completed", "talent_marked_completed", "booking_type", "payment_completed"]
    def get_subcategories(self, obj):
        try:
            user_sub_cat = TalentDetailsModel.objects.filter(user_id=obj.talent_id).first()
            sub_cat = TalentSubCategoryModel.objects.filter(id__in=user_sub_cat.sub_categories).values_list("name")
            result = ", ".join([i[0] for i in sub_cat])
            return result    
        except:
            return None
    def get_final_price(self, obj):
        if obj.final_price is None:
            return None
        else:
            val = round((obj.final_price), 2)
            return val
    def get_status(self, obj):
        try:
            return obj.get_status_display()
        except:
            return None
    def get_track_booking(self, obj):
        try:
            return obj.get_track_booking_display()
        except:
            return None
    def get_service_price(self, obj):
        try:
            val = ContactUsModel.objects.first()
            return float(val.service_price)
            # if obj.final_price is None:
            #     return round(float(val.service_price), 2)
            # else:
            #     return round(((obj.final_price*float(val.service_price))/100),2)
        except:
            return None

class NotificationsSerializer(serializers.ModelSerializer):
    booking_id = ShowBookingDetailsSerializer()
    sent_date = serializers.SerializerMethodField()
    sent_time = serializers.SerializerMethodField()
    class Meta:
        model = AppNotificationModel
        fields = ["id", "user", "notification_type", "title", "booking_id", "sent_date", "sent_time"]
    def get_sent_date(self, obj):
        try:
            return obj.created_at.date()
        except:
            return obj.created_at
    def get_sent_time(self, obj):
        try:
            return obj.created_at.time()
        except:
            return obj.created_at
            