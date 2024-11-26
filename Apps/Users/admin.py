from django.contrib import admin
from .models import Users


# Creamos un método para mostrar los grupos
def get_user_groups(obj):#obj se refiere al usuario actual que se está mostrando.
    return ", ".join([group.name for group in obj.groups.all()])


get_user_groups.short_description = 'Grupo asignado'  #short_description: Este es un atributo especial que puedes asignar a un método en Django cuando se usa en el list_display del Django Admin


# Personalizamos la vista del panel de administración para los usuarios
@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    readonly_fields = ('actualizado',)
    list_display = ('username', 'first_name', 'last_name', 'email', 'actualizado', get_user_groups)
    
    # Configuramos los campos que aparecerán en el formulario de edición
    fields = ('username', 'first_name', 'last_name', 'email' , 'is_staff', 'is_active', 'actualizado', 'groups')
    
    # Esto hace que el campo 'groups' se vea como una lista de selección múltiple en el formulario
    filter_horizontal = ('groups',)  