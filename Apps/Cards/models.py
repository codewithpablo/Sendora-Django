from django.db import models
from Apps.Accounts.models import BankAccounts, SendoraAccounts

# Create your models here.

class SenodoraCards(models.Model):
    numero_tarjeta = models.CharField(max_length=19, unique=True)
    fecha_expiracion = models.DateField()
    cvv = models.CharField(max_length=4)
    cuenta = models.OneToOneField(SendoraAccounts, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Sendora"
        verbose_name_plural = "Sendora"
        
    def __str__(self):
        return f"Tarjeta de {self.cuenta.titular} en la cuenta del banco {self.cuenta.banco}"
    
class BankCards(models.Model):
    numero_tarjeta = models.CharField(max_length=19, unique=True)
    fecha_expiracion = models.DateField()
    cvv = models.CharField(max_length=4)
    cuenta = models.OneToOneField(BankAccounts, on_delete=models.CASCADE)
        
    class Meta:
        verbose_name = "Bancaria"
        verbose_name_plural = "Bancaria"
    
def __str__(self):
    return f"Tarjeta de {self.cuenta.titular} en la cuenta del banco {self.cuenta.banco}"
    