from django.urls import path
from .views import (
    TraineeListView,
    TraineeCreateView,
    TraineeDeleteView,
    TraineeUpdateView,
)

urlpatterns = [
    path("", TraineeListView.as_view(), name="trainee_list"),
    path("add/", TraineeCreateView.as_view(), name="add_trainee"),
    path("delete/<int:pk>/", TraineeDeleteView.as_view(), name="delete_trainee"),
    path("update/<int:pk>/", TraineeUpdateView.as_view(), name="update_trainee"),
]
