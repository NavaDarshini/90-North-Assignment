from django.db import models
from App.models.baseModel import BaseModel
from App.models import ChatSessionModel, UserModel

class ChatStorageModel(BaseModel):
    session = models.ForeignKey(ChatSessionModel, on_delete=models.CASCADE)
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name="user")
    message = models.TextField(default="")
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Chat Storage"
