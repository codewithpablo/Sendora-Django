from django.contrib import admin
from .models import Incomes

@admin.register(Incomes)
class IncomesAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de ingresos
    list_display = ('id', 'monto', 'origen', 'fecha_y_hora')
    
    # Campos que serán utilizables para buscar en el admin
    search_fields = ('origen__nombre', 'fecha_y_hora')  # 'nombre' es un ejemplo, ajusta según el campo que quieras buscar en Accounts.
    
    # Filtros disponibles en la barra lateral
    list_filter = ('fecha_y_hora', 'origen')