from django.urls import psth
from . import views

urlpatterns = [
    path('', views.port_list, name='post_list'),
]