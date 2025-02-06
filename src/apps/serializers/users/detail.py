from rest_framework import serializers

import src.core.models as models


class DetailCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "first_name", "last_name", "username", "role", "date_joined")

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["date_joined"] = instance.date_joined.strftime("%Y-%m-%d %H:%M")
        return data