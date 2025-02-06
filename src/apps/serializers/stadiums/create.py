from rest_framework import serializers

import src.core.models as models
import src.apps.serializers.base as base


class CreateStadionSerializer(serializers.ModelSerializer):
    contacts = serializers.ListSerializer(
        child=base.build_relational_model_serializer(
            model_=models.StadionContact, fields_=("f_name", "phone"))
    )
    images = serializers.ListSerializer(child=serializers.IntegerField())

    class Meta:
        model = models.Stadion
        exclude = ("updated_by", "created_by")
