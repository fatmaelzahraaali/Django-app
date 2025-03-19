from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import track_update, TrackViewSet

router = DefaultRouter()
router.register(r"tracks", TrackViewSet)  # ViewSet for managing tracks

urlpatterns = [
    path(
        "update/<int:pk>/", track_update, name="track_update"
    ),  # Function-based view for updates
    path("", include(router.urls)),  # ViewSet routes
]
