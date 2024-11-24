from django.db import models
from Apps.Users.models import Users
from Apps.Banks.models import Banks
import random
random.seed()



# Configurar el locale para usar el formato deseado
import locale
locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')  # Cambia a un locale adecuado para tu sistema

# Create your models here.


class CorporateAccounts(models.Model):
    alias = models.CharField(max_length=50)
    titular = models.ForeignKey(Users, on_delete=models.CASCADE,)
    saldo = models.IntegerField(default=0)
    banco  = models.ForeignKey(Banks, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.titular} - {self.banco}  "
    
    class Meta: 
        verbose_name = "Corporativa"
        verbose_name_plural = "Corporativas"
    
    # Aseguramos que cada usuario solo pueda tener una cuenta por banco
    constraints = [
            models.UniqueConstraint(fields=['titular', 'banco'], name='unique_user_bank_account')
        ]
    
    def __str__(self):
        
        return f" {self.titular} - {self.banco}  "
    


        
#--------------------------------------------------------------------------------------------------------

# Generar un número aleatorio al momento de instanciar el modelo
def generar_saldo_aleatorio():
    random.seed()  # Solo se ejecuta una vez, cuando se genera el saldo
    return round(random.uniform(0, 1000000), 2)

class BankAccounts(models.Model):
    alias = models.CharField(max_length=50)
    titular = models.ForeignKey(Users, on_delete=models.CASCADE,)
    saldo = models.DecimalField(
        default=generar_saldo_aleatorio,  # Usamos la función para generar el saldo aleatorio
        decimal_places=2,
        max_digits=10
    )
    banco  = models.ForeignKey(Banks, on_delete=models.CASCADE, null=True)
    
    
    
    
    def __str__(self):
        saldo_formateado = f"{self.saldo:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        return f"{self.banco}: ${str(saldo_formateado)}  "
    
    class Meta: 
        verbose_name = "Bancaria"
        verbose_name_plural = "Bancarias"
        
        
#--------------------------------------------------------------------------------------------------------
class SendoraAccounts(models.Model):
    alias = models.CharField(max_length=50)
    titular = models.OneToOneField(Users, on_delete=models.CASCADE)
    saldo = models.IntegerField(default=0)
    
   #Metodo para transferir de una cuenta a otra
    def transferir(self, cuenta_destino, monto):
        #Si tenes el dinero sufieciente para transferir
        if self.saldo >= monto:
            # Restame el monto de la cuenta de origen
            self.saldo -= monto
            # Suma el monto a la cuenta de destino
            cuenta_destino.saldo += monto
            # Guardamelos cambios de ambas cuentas en la base de datos
            self.save()
            
            cuenta_destino.save()
            return True
        else:
            # Si el saldo no es suficiente
            return False
    
    
    def __str__(self):
        return f"{self.alias} - {self.titular}  "
    
    class Meta: 
        verbose_name = "Sendora"
        verbose_name_plural = "Sendora"