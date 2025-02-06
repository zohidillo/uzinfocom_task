from rest_framework import serializers

import src.core.models as models


class ListRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Region
        fields = ("id", "name")


class ListDistrictSerializer(serializers.ModelSerializer):
    region = ListRegionSerializer()

    class Meta:
        model = models.District
        fields = ("id", "region", "name")
