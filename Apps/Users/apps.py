from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Apps.Users'

    verbose_name = "Usuarios"
    
    # La funcion ready() se llama cuando se carga la aplicacion, en este caso estamos importando las señales desde signals.py
    def ready(self):
        import Apps.Users.signals
        
        
