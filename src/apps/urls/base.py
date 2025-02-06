from django.urls import path, include

urlpatterns = [
    path("users/", include("src.apps.urls.users")),
    path("booking/", include("src.apps.urls.booking")),
    path("stadion/", include("src.apps.urls.stadion")),
    path("region/", include("src.apps.urls.utils.region")),
    path("district/", include("src.apps.urls.utils.district")),
    path("file/", include("src.apps.urls.utils.file_manager")),
]
