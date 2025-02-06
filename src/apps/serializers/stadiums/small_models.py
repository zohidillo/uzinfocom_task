import src.core.models as models
from rest_framework import serializers
import src.apps.serializers.base as base


class BookingTimes(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ("id", "booking_start_date", "booking_end_date")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["booking_start_date"] = instance.booking_start_date.strftime("%Y-%m-%d %H:%M")
        data["booking_end_date"] = instance.booking_end_date.strftime("%Y-%m-%d %H:%M")
        return data


class StadionContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StadionContact
        fields = ("id", "f_name", "phone")


class StadionImageSerializer(serializers.ModelSerializer):
    image = base.build_relational_model_serializer(model_=models.FileManager, fields_=("id", "image"))

    class Meta:
        model = models.StadionImages
        fields = ("id", "image")
