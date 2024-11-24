from django.contrib.auth.models import Group
from .models import Users
from django.dispatch import receiver
from django.db.models.signals import post_save

@receiver(post_save, sender=Users)
def add_user_to_default_group(sender, instance, created, **kwargs):
    if created:  # Solo cuando se crea un nuevo usuario
        # Crear o verificar el grupo "Usuarios"
        try:
            users_group = Group.objects.get(name="Usuario")
        except Group.DoesNotExist:
            users_group = Group.objects.create(name="Usuario")
        
        # Crear o verificar el grupo "Administradores"
        try:
            admins_group = Group.objects.get(name="Administrador")
        except Group.DoesNotExist:
            admins_group = Group.objects.create(name="Administrador")

       
        # Si el usuario es un superusuario lo incluimos al grupo de administradores
        if instance.is_superuser:
            instance.groups.add(admins_group)
        #De lo contrario, lo incluimos al grupo de usuarios
        else:
             instance.groups.add(users_group)
