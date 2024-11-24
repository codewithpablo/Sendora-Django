from django.urls import path
from . import views

urlpatterns = [
    path("", views.income, name="income"),
    path("ingresar_dinero", views.ingresar_dinero, name="ingresar_dinero"),
    path("ver_ingreso/<int:ingreso_id>", views.ver_ingreso, name="ver_ingreso")
]