from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class DetailStadionApiView(RetrieveAPIView, GenericViewSet):
    queryset = models.Stadion.objects.select_related(
        "region", "district", "created_by").prefetch_related("contacts", "images")
    serializer_class = serializers.DetailStadionSerializer
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission | shared.ClientPermission, )
