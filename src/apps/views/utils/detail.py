from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import RetrieveAPIView

import src.core.models as models
import src.apps.serializers as serializers


class DetailFileManagerApiView(RetrieveAPIView, GenericViewSet):
    queryset = models.FileManager.objects.all()
    serializer_class = serializers.DetailFileManagerSerializer
