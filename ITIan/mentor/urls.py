from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.mentor_list, name='mentor_list'),
    path('add/', views.add_mentor, name='add_mentor'),
]
