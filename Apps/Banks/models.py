from django.db import models

class Banks(models.Model):
    nombre = models.CharField(max_length=50)  # Nombre del banco
    email = models.EmailField(null=True, blank=True)  # Correo electrónico de contacto
    website = models.URLField(null=True, blank=True)  # Sitio web oficial
    
    def __str__(self):
        return self.nombre
    
    class Meta: 
        verbose_name = "Banco"
        verbose_name_plural = "Bancos"