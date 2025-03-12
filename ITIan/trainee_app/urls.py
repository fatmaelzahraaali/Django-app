from django.urls import path
from . import views
from .views import add_trainee, update_trainee

urlpatterns = [
    path("", views.trainee_list, name="trainee_list"),
    path("add/", views.add_trainee, name="add_trainee"),
    path("update/<int:id>/", views.update_trainee, name="update_trainee"),
    path("delete/<int:id>/", views.delete_trainee, name="delete_trainee"),
]
