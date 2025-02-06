import src.core.models as models
from rest_framework import serializers
import src.apps.serializers.base as base


class StadionContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StadionContact
        fields = ("id", "f_name", "phone")


class StadionImageSerializer(serializers.ModelSerializer):
    image = base.build_relational_model_serializer(model_=models.FileManager, fields_=("id", "image"))

    class Meta:
        model = models.StadionImages
        fields = ("id", "image")
