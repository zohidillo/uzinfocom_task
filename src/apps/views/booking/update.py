from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.viewsets import GenericViewSet

from django.db import transaction

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class UpdateBookingApiView(UpdateAPIView, GenericViewSet):
    queryset = models.Booking.objects.select_related("stadion", "created_by")
    serializer_class = serializers.UpdateBookingSerializer
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission | shared.ClientPermission,)

    def update(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        instance = self.get_object()

        with transaction.atomic():
            instance.updated_by = user
            instance.stadion_id = data.pop("stadion", instance.stadion_id)
            instance.booking_start_date = data.pop("booking_start_date", instance.booking_start_date)
            instance.booking_end_date = data.pop("booking_end_date", instance.booking_end_date)

            instance.save()
            obj_data = serializers.DetailBookingSerializer(instance).data
            return Response(obj_data, status.HTTP_200_OK)

        try:
            pass
        except Exception as e:
            return Response({"error": str(e)}, status.HTTP_400_BAD_REQUEST)
