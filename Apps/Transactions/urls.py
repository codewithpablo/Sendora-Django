
from django.urls import path
from . import views



urlpatterns = [
    path("", views.transactions, name="transactions"),
    path("maketransaction/", views.realizar_transferencia, name="maketransaction"),
    path("ver_comprobante/<int:id_comprobante>", views.ver_comprobante, name="ver_comprobante"),
    path('marcarcomofavorito/<int:account_id>/', views.marcar_favorita, name='marcarcomofavorito'),
]