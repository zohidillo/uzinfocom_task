from rest_framework.routers import SimpleRouter

from src.apps.views.utils import *

router = SimpleRouter()
router.register("list", ListDistrictApiView)

urlpatterns = [] + router.urls
