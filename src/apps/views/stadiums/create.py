from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import CreateAPIView

from django.db import transaction

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class CreateStadionApiView(CreateAPIView, GenericViewSet):
    queryset = models.Stadion.objects.select_related("region", "district")
    serializer_class = serializers.CreateStadionSerializer
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission,)

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        region = data.pop("region")
        district = data.pop("district")
        contacts = data.pop("contacts", [])
        images = data.pop("images", [])

        try:
            with transaction.atomic():
                obj = models.Stadion.objects.create(created_by=user, region_id=region, district_id=district, **data)

                contact_list = [models.StadionContact(stadion=obj, created_by=user, **i) for i in contacts]
                image_list = [models.StadionImages(stadion=obj, created_by=user, image_id=i) for i in images]

                models.StadionContact.objects.bulk_create(contact_list)
                models.StadionImages.objects.bulk_create(image_list)
                obj_data = serializers.DetailStadionSerializer(obj).data
                return Response(obj_data, status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)


"""
{
  "contacts": [
    {
      "f_name": "Men",
      "phone": "123"
    }
  ],
  "images": [
    1
  ],
  "name": "shat",
  "address": "3432",
  "length": "13.1",
  "width": "15.5",
  "varata_height": "2",
  "varata_width": "4",
  "price": "150000",
  "work_start_time": "15:00",
  "work_end_time": "16:00",
  "description": "tesk",
  "region": 1,
  "district": 1
}
"""
