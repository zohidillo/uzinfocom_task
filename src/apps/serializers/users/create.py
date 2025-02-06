from rest_framework import serializers

import src.core.models as models


class CreateCustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ("id", "first_name", "last_name", "username", "password", "role")
