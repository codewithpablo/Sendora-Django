from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    actualizado = models.DateTimeField(auto_now=True)  # Se actualiza automáticamente
    
    class Meta:
        db_table = "users"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
        