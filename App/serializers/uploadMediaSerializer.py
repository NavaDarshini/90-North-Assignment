from rest_framework import serializers
from App.models.uploadMediaModel import UploadMediaModel

class CreateUpdateUploadMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = UploadMediaModel
        fields = ["id", "media_file_url", "media_file_type", "media_file_name", "is_video"]


