from rest_framework import serializers

import src.core.models as models


class CreateFileManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FileManager
        fields = ("id", "image")

    # def create(self, validated_data):
    #     request = self.context.request
    #     return models.FileManager.objects.create(created_by=request.user, **validated_data)
