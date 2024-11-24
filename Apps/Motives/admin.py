from django.contrib import admin
from .models import Motives

@admin.register(Motives)
class MotivesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')  # Muestra el ID y el nombre en la lista de elementos.
    search_fields = ('nombre',)     # Permite buscar por el nombre.
    list_per_page = 25              # Define la cantidad de elementos por página.