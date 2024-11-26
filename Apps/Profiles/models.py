from django.db import models
from Apps.Users.models import Users
from django.db.models.signals import post_save
from Apps.Accounts.models import SendoraAccounts

# Models
class Profiles(models.Model):
    usuario = models.OneToOneField(Users, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to='users/', verbose_name="Foto de perfil",  default="users/no-photo.png")
    dni = models.CharField(max_length=50, default=" ", blank=True)
    phone_number = models.CharField(max_length=50, default=" ", blank=True)
    fecha_nacimiento =  models.DateField(null=True, blank=True)
    
    #cuentas_ favoritas como atributo de Profiles
    # va a permitir que un usuario tenga múltiples cuentas favoritas, y que cada cuenta pueda ser favorita de varios usuarios si fuera necesario.
    cuentas_favoritas = models.ManyToManyField(SendoraAccounts, blank=True)
    
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        
    def __str__(self):
        return self.usuario.username
    

# Creamos un perfil automaticamente despues de que se crea un usuario con una funcion personalizada
def create_a_profile(sender, instance, created, **kwargs, ):
    if created:
        Profiles.objects.create(usuario=instance)
        

# Conectamos la señal para crear el perfil    
post_save.connect(create_a_profile, sender=Users)

#Como decidi  no usar un archivo signals.py en Profiles y coloque las señales directamente en models.py, no es necesario importar en apps.py en el metodo ready()