from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import GenericViewSet

from django.db import transaction

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class UpdateStadionApiView(UpdateAPIView, GenericViewSet):
    queryset = models.Stadion.objects.select_related("region", "district")
    serializer_class = serializers.UpdateStadionSerializer
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission,)

    def update(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        instance = self.get_object()
        images = data.pop("images", [])
        contacts = data.pop("contacts", [])

        try:
            with transaction.atomic():
                instance.updated_by = user
                instance.region_id = data.pop("region", instance.region_id)
                instance.district_id = data.pop("district", instance.district_id)

                for attr, value in data.items():
                    setattr(instance, attr, value)

                if contacts:
                    instance.contacts.all().delete()
                    contact_list = [models.StadionContact(stadion=instance, updated_by=user, **i) for i in contacts]
                    models.StadionContact.objects.bulk_create(contact_list)

                if images:
                    instance.images.all().delete()
                    image_list = [models.StadionImages(stadion=instance, updated_by=user, image_id=i) for i in images]
                    models.StadionImages.objects.bulk_create(image_list)
                instance.save()

                obj_data = serializers.DetailStadionSerializer(instance).data
                return Response(obj_data, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
