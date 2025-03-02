from App.models.userModel import UserModel
from App.models.baseModel import BaseModel
from App.models.bookingTalentModel import BookingTalentModel
from django.db import models
# from App.utils.choiceFields import NOTIFICATION_TYPE_CHOICES

class AppNotificationModel(BaseModel):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    notification_type = models.IntegerField(default=2)
    title = models.TextField()
    booking_id = models.ForeignKey(BookingTalentModel, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        db_table = "App Notifications"