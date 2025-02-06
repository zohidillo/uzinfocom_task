from django.urls import path
from rest_framework.routers import SimpleRouter

from src.apps.views.users import *

router = SimpleRouter()
router.register("create", CreateCustomUserApiView)

urlpatterns = [
                  path("get-me/", GetMeApiView.as_view())
              ] + router.urls
