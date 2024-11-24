from django.db import models
from Apps.Accounts.models import BankAccounts, SendoraAccounts


# Create your models here.

class Incomes(models.Model):
    monto = models.FloatField()
    origen = models.ForeignKey(BankAccounts, on_delete=models.CASCADE)
    destino = models.ForeignKey(SendoraAccounts, on_delete=models.CASCADE, null=True)
    fecha_y_hora = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = "Ingreso"
        verbose_name_plural = "Ingresos"
        
    def __str__(self):
        return f"Ingreso N°{self.id}. De {self.origen} a tu cuenta Sendora. Fecha: {self.fecha_y_hora}"
    