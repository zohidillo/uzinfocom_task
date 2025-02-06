from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class ListBookingApiView(ListAPIView, GenericViewSet):
    queryset = models.Booking.objects.select_related("created_by", "stadion")
    serializer_class = serializers.ListBookingSerializer
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission,)

    def get_queryset(self):
        user = self.request.user
        qs = super().get_queryset()
        if user.role == models.CONSTANTS.ROLE.stadion_owner:
            qs = qs.filter(stadion__created_by=user)
        return qs
