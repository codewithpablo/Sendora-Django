
from django.urls import path
from .views import home, redirect_to_home

urlpatterns = [
    path("", redirect_to_home, name="redirect_to_home"),
    path("home/", home, name="home")
]