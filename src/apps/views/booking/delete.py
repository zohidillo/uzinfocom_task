from rest_framework.generics import DestroyAPIView
from rest_framework.viewsets import GenericViewSet

import src.shared as shared
import src.core.models as models


class DeleteBookingApiView(DestroyAPIView, GenericViewSet):
    queryset = models.Booking.objects.all()
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission | shared.ClientPermission,)
