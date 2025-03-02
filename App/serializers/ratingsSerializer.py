from rest_framework import serializers
from App.models.ratingsModel import ReviewAndRatingsModel
from App.serializers.chatSerializer import UserDetailsSerializer
from django.db.models import Avg

class AddRatingSerializer(serializers.ModelSerializer):
	# client = serializers.HiddenField(default=serializers.CurrentUserDefault())
	class Meta:
		model = ReviewAndRatingsModel
		fields = ["id", "talent", "client", "review", "rating", "best_liked", "booking", "given_by"]
		
class GetRatingSerializer(serializers.ModelSerializer):
	client = UserDetailsSerializer()
	talent = UserDetailsSerializer()
	class Meta:
		model = ReviewAndRatingsModel
		fields = ["id", "talent", "client", "review", "rating"]