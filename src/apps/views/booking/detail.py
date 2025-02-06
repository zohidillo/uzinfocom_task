from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class DetailBookingApiView(RetrieveAPIView, GenericViewSet):
    queryset = models.Booking.objects.select_related("stadion", "created_by")
    serializer_class = serializers.DetailBookingSerializer
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission | shared.ClientPermission,)
