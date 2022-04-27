from django.urls import psth
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]