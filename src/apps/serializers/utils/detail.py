from rest_framework import serializers

import src.core.models as models


class DetailFileManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FileManager
        fields = ("id", "image", "created_at")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"] = instance.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return data
