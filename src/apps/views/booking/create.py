from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated

import src.core.models as models
import src.apps.serializers as serializers


class CreateBookingApiView(CreateAPIView, GenericViewSet):
    queryset = models.Booking.objects.select_related("created_by", "stadion")
    serializer_class = serializers.CreateBookingSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        data = super().get_serializer_context()
        data["request"] = self.request
        return data

