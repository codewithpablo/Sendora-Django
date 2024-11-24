from django.db import models

# Create your models here.

class Motives(models.Model):
    nombre = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = "Motivo"
        verbose_name_plural = "Motivos"
    
    def __str__(self):
        return self.nombre