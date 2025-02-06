from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

from django_filters.rest_framework import DjangoFilterBackend

import src.shared as shared
import src.core.models as models
import src.apps.serializers as serializers


class ListStadionApiView(ListAPIView, GenericViewSet):
    queryset = models.Stadion.objects.select_related(
        "region", "district", "created_by").prefetch_related("contacts", "images")
    serializer_class = serializers.ListStadionSerializer
    permission_classes = (shared.AdminPermission | shared.StadionOwnerPermission | shared.ClientPermission,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = shared.StadionFilterSet
