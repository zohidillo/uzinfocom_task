from src.apps.serializers.stadiums.small_models import *


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
        data["created_at"] = instance.created_at.strftime("%Y-%m-%d %H:%M")
        return data
