from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

import src.core.models as models
import src.apps.serializers as serializers


class GetMeApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        obj = serializers.DetailCustomUserSerializer(user)
        return Response(obj.data)
