from src.apps.serializers.stadiums.small_models import *
from datetime import datetime


class BookingTimes(serializers.ModelSerializer):
    class Meta:
        model = models.Booking
        fields = ("booking_start_date", "booking_end_date")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["booking_start_date"] = instance.booking_start_date.strftime("%Y-%m-%d %H:%M")
        data["booking_end_date"] = instance.booking_end_date.strftime("%Y-%m-%d %H:%M")
        return data


class ListStadionSerializer(serializers.ModelSerializer):
    contacts = StadionContactSerializer(many=True)
    images = StadionImageSerializer(many=True)
    region = base.build_relational_model_serializer(models.Region, fields_=("id", "name"))
    district = base.build_relational_model_serializer(models.District, fields_=("id", "name"))

    class Meta:
        model = models.Stadion
        fields = (
            "id", "name", "region", "district",
            "address", "contacts", "images", "price",
            "work_start_time", "work_end_time"
        )

    def to_representation(self, instance):
        data = super().to_representation(instance)
        today = datetime.today()
        data["booking_times"] = BookingTimes(instance.bookings.all().filter(
            booking_start_date__gte=today), many=True).data
        return data
