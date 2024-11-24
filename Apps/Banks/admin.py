from django.contrib import admin
from .models import Banks

@admin.register(Banks)
class BanksAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'website')  # Muestra las columnas principales
    search_fields = ('nombre', 'email')  # Habilita la búsqueda por nombre y correo
    list_filter = ('email',)  # Agrega un filtro por correo electrónico

