from django.urls import path
from .views import log_in, log_out, sign_up

urlpatterns = [
    path("login/", log_in, name="login"),
    path("logout/", log_out, name="logout"),
    path("signup/", sign_up, name="signup")
]
