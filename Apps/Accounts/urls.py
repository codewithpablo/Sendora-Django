from django.urls import path
from . import views

urlpatterns = [
    path('', views.accounts, name="accounts"),
    path("addbankaccount/", views.addbankaccount, name="addbankaccount"),
    path("deslinkbankaccount/<int:account_id>/", views.deslink, name="deslink")
]