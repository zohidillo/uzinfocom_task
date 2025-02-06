from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import CreateAPIView

from django.db import transaction

import src.core.models as models
import src.apps.serializers as serializers


class CreateCustomUserApiView(CreateAPIView, GenericViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CreateCustomUserSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        requested_user = request.user
        with transaction.atomic():
            if f"{requested_user}" == "AnonymousUser":
                role = data.pop("role")
            else:
                data["role"] = models.CONSTANTS.ROLE.stadion_owner
            password = data.pop("password")
            user = models.CustomUser.objects.create_user(**data)
            user.set_password(password)
            user.save()
            obj = self.get_serializer(user)
            return Response(obj.data)
