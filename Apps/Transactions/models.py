from django.db import models
from Apps.Users.models import Users
from Apps.Motives.models import Motives

# Create your models here.

class Transactions(models.Model):
    monto = models.IntegerField()
    remitente = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="transaciones_como_remitente")
    destinatario = models.ForeignKey(Users, on_delete=models.CASCADE, related_name="transaciones_como_destinatario")
    fecha_y_hora = models.DateTimeField(auto_now_add=True)
    motivo = models.ForeignKey(Motives, on_delete=models.CASCADE, null=True)
    
    class Meta:
        verbose_name = "Transacion"
        verbose_name_plural = "Transacciones"
        
        
    def __str__(self):
        return f"Transferencia numero {self.id}"
