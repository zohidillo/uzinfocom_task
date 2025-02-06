from rest_framework.routers import SimpleRouter

from src.apps.views.utils import *

router = SimpleRouter()
router.register("detail", DetailFileManagerApiView, basename="detail-file")
router.register("create", CreateFileManagerApiView, basename="create-file")

urlpatterns = [] + router.urls
