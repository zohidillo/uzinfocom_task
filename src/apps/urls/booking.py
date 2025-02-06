from rest_framework.routers import SimpleRouter

from src.apps.views.booking import *

router = SimpleRouter()
router.register("list", ListBookingApiView, basename="list-booking")
router.register("update", UpdateBookingApiView, basename="update-booking")
router.register("create", CreateBookingApiView, basename="create-booking")
router.register("delete", DeleteBookingApiView, basename="delete-booking")
router.register("detail", DetailBookingApiView, basename="detail-booking")

urlpatterns = [] + router.urls
