from src.apps.serializers.base import *

import src.core.models as models


class ListBookingSerializer(serializers.ModelSerializer):
    stadion = build_relational_model_serializer(models.Stadion, fields_=("id", "name"))
    created_by = build_relational_model_serializer(models.CustomUser,
                                                   fields_=("id", "username", "first_name", "last_name"))

    class Meta:
        model = models.Booking
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["created_at"] = instance.created_at.strftime("%Y-%m-%d %H:%M")
        data["updated_at"] = instance.updated_at.strftime("%Y-%m-%d %H:%M")
        data["booking_end_date"] = instance.booking_end_date.strftime("%Y-%m-%d %H:%M")
        data["booking_start_date"] = instance.booking_start_date.strftime("%Y-%m-%d %H:%M")
        return data
