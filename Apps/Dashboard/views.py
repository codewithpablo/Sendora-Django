from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps.Accounts.models import BankAccounts, SendoraAccounts
from django.db.models import Sum
from Apps.Transactions.models import Transactions
from django.db.models import Q


#!Funcion para renderizar el dashboard
@login_required
def dashboard(request):
    #Usuario logueado
    usuario_logueado = request.user
    # Cantidad de cuentas
    cantidad_cuentas  = BankAccounts.objects.filter(titular=usuario_logueado).count()
    #Balance total 
    balance_total = round(BankAccounts.objects.filter(titular=usuario_logueado).aggregate(total_balance=Sum('saldo'))['total_balance'] or 0, 2)
    #Transacciones recibidias o enviadas por el usuario logueado
    todas_transacciones = Transactions.objects.filter(Q(remitente=usuario_logueado) | Q(destinatario=usuario_logueado)).order_by('-fecha_y_hora')
    
    #si el usuario esta autenticado devolveme el slado de su cuenta
    if request.user.is_authenticated:
        cuenta_sendora = SendoraAccounts.objects.get(titular=request.user)
        saldo = cuenta_sendora.saldo
    else:
        saldo = 0  
    
    context = {
        
        "cuenta_sendora_saldo": saldo,
        "transactions":  todas_transacciones ,
        "cantidad_cuentas_asociadas": cantidad_cuentas,
        "balance_total": balance_total,
        "todas_transacciones": todas_transacciones
    }
    return render(request, "dashboard.html", context)

