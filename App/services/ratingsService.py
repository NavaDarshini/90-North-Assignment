from App.models.ratingsModel import ReviewAndRatingsModel
from App.serializers.ratingsSerializer import AddRatingSerializer, GetRatingSerializer
from App.models.bookingTalentModel import BookingTalentModel
from App.utils import messages
from App.models.userModel import UserModel
from App.models.ratingsModel import ReviewAndRatingsModel
from django.db.models import Avg
from datetime import datetime, timedelta

class RatingService():
    def add_rating(self, request):
        TALENT, CLIENT = False, False
        if request.user.role == 1:
            TALENT = True
            request.data["client"] = request.user.id
            request.data["given_by"] = 1
        elif request.user.role == 2:
            CLIENT = True
            request.data["talent"] = request.user.id
            request.data["given_by"] = 2
        booking_id = request.data["booking"]
        try:
            booking = BookingTalentModel.objects.get(id=booking_id)
        except BookingTalentModel.DoesNotExist:
            return {"data": None, "message": "Record not found", "status": 400}
        serializer = AddRatingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            if TALENT:
                booking.rating_by_client = True
                try:
                    talent = UserModel.objects.get(id=request.data["talent"])
                    all_talent_ratings = ReviewAndRatingsModel.objects.filter(talent=request.data["talent"]).\
                                                                        aggregate(avg_rating=Avg("rating"))
                    talent.average_rating = all_talent_ratings["avg_rating"]
                    talent.save()
                except:
                    pass    
            elif CLIENT:
                booking.rating_by_talent = True
                try:
                    client = UserModel.objects.get(id=request.data["client"])
                    all_client_ratings = ReviewAndRatingsModel.objects.filter(client=request.data["client"]).\
                                                                        aggregate(avg_rating=Avg("rating"))
                    client.average_rating = all_client_ratings["avg_rating"]
                    client.save()
                except:
                    pass
            booking.save()
            return {"data": serializer.data, "message": messages.ADDED_RATING, "status": 200}
        return {"data": serializer.errors, "message": messages.WENT_WRONG, "status": 400}
    
    def get_talent_ratings(self, request, talent_id):
        ratings = ReviewAndRatingsModel.objects.filter(talent=talent_id)
        # if "key" == 2:
        #     date = datetime.now() - timedelta(days=7)
        #     ratings = ratings.filter(created_at__gte=date)
        # if "key" == 3:
        #     pass    
        serializer = GetRatingSerializer(ratings, many=True)
        return {"data": serializer.data, "message": "Ratings fetched successfully", "status": 200}

    def get_talent_ratings_by_key(self, request, talent_id):
        ratings = ReviewAndRatingsModel.objects.filter(talent=talent_id)
        if request.data["key"] == 2:
            checking_date = datetime.now()-timedelta(days=7)
            ratings = ratings.exclude(created_at__lt=checking_date)
        if "key" == 3:
            pass
        serializer = GetRatingSerializer(ratings, many=True)
        return {"data": serializer.data, "message": "Ratings fetched successfully", "status": 200}

    def get_all_ratings(self, request):
        try:
            rating = ReviewAndRatingsModel.objects.all()
            serializer = GetRatingSerializer(rating)
            return {"data":serializer.data,"message":messages.FETCH,"status":200}
        except Exception as e:
            return {"data":None,"message":messages.WENT_WRONG,"status":400}