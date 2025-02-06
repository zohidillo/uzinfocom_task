from rest_framework.routers import SimpleRouter

from src.apps.views.stadiums import *

router = SimpleRouter()
router.register("list", ListStadionApiView, basename="list-stadion")
router.register("create", CreateStadionApiView, basename="create-stadion")
router.register("detail", DetailStadionApiView, basename="detail-stadion")
router.register("update", UpdateStadionApiView, basename="update-stadion")
router.register("delete", DeleteStadionApiView, basename="delete-stadion")

urlpatterns = [] + router.urls
