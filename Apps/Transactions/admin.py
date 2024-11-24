from django.contrib import admin
from .models import Transactions

# Register your models here.


@admin.register(Transactions)
class TransactionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'monto', 'remitente', 'destinatario', 'fecha_y_hora', 'motivo',)
    list_filter = ( 'fecha_y_hora', 'motivo')
    search_fields = ('remitente__username', 'destinatario__username', 'motivo__nombre')
    date_hierarchy = 'fecha_y_hora'