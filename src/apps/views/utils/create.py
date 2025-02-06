from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import CreateAPIView

import src.core.models as models
import src.apps.serializers as serializers


class CreateFileManagerApiView(CreateAPIView, GenericViewSet):
    queryset = models.FileManager.objects.all()
    serializer_class = serializers.CreateFileManagerSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        images = data.pop("image")
        ids = []
        for i in images:
            obj = models.FileManager.objects.create(image=i)
            ids.append(obj.id)

        return Response({"ids": ids})
