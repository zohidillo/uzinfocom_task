from src.apps.serializers.base import *

import src.core.models as models


class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        exclude = ("updated_at", "updated_by", "created_by")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"] = instance.created_at.strftime("%Y-%m-%d %H:%M")
        data["updated_at"] = instance.updated_at.strftime("%Y-%m-%d %H:%M")
        data["booking_end_date"] = instance.booking_end_date.strftime("%Y-%m-%d %H:%M")
        data["booking_start_date"] = instance.booking_start_date.strftime("%Y-%m-%d %H:%M")
        return data

    def create(self, validated_data):
        request = self.context.get("request")
        booking = models.Booking.objects

        return booking.create(
            created_by=request.user, stadion=validated_data.pop("stadion"), **validated_data
        )
