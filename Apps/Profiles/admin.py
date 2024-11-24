from django.contrib import admin
from .models import Profiles

@admin.register(Profiles)
class ProfilesAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de registros
    list_display = ('usuario', 'dni', 'phone_number', 'fecha_nacimiento')

    # Hacer que se pueda buscar por estos campos
    search_fields = ('usuario__username', 'dni', 'phone_number')