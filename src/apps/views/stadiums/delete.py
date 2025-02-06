from rest_framework.generics import DestroyAPIView
from rest_framework.viewsets import GenericViewSet

import src.shared as shared
import src.core.models as models


class DeleteStadionApiView(DestroyAPIView, GenericViewSet):
    queryset = models.Stadion.objects.all()
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission,)
