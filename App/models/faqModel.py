from django.db import models
from App.models.baseModel import BaseModel

class FAQModel(BaseModel):
    question = models.TextField()
    answer = models.TextField()
    class Meta:
        db_table = "Faqs"