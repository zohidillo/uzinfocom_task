from src.apps.serializers.stadiums.small_models import *
from datetime import datetime


class DetailStadionSerializer(serializers.ModelSerializer):
    contacts = StadionContactSerializer(many=True)
    images = StadionImageSerializer(many=True)
    region = base.build_relational_model_serializer(models.Region, fields_=("id", "name"))
    district = base.build_relational_model_serializer(models.District, fields_=("id", "name"))
    created_by = base.build_relational_model_serializer(
        models.CustomUser, fields_=("id", "username", "first_name", "last_name")
    )

    class Meta:
        model = models.Stadion
        exclude = ("updated_at", "updated_by")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        today = datetime.today()
        data["booking_times"] = BookingTimes(instance.bookings.all().filter(
            booking_start_date__gte=today), many=True).data
        data["created_at"] = instance.created_at.strftime("%Y-%m-%d %H:%M")
        return data
