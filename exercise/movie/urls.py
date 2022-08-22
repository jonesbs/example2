from django.urls import include, path
from rest_framework import routers

from .views import MovieStatViewset, MovieViewset

router = routers.DefaultRouter()
router.register(r"movie", MovieViewset, basename="movie")
router.register(r"movie-stats", MovieStatViewset, basename="movie-stats")

app_name = "movie"
urlpatterns = [
    path("", include(router.urls)),
]
