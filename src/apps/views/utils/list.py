from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet

import src.core.models as models
import src.apps.serializers as serializers


class ListRegionApiView(ListAPIView, GenericViewSet):
    queryset = models.Region.objects.all()
    serializer_class = serializers.ListRegionSerializer


class ListDistrictApiView(ListAPIView, GenericViewSet):
    queryset = models.District.objects.all()
    serializer_class = serializers.ListDistrictSerializer
