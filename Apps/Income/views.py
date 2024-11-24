from django.shortcuts import render, redirect, get_object_or_404
from .models import Incomes
from decimal import InvalidOperation, Decimal
from Apps.Accounts.models import BankAccounts, SendoraAccounts
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def income(request):

    # Traeme  todas las cuentas bancarias del usuario actual
    cuentas_bancarias = BankAccounts.objects.filter(titular=request.user)

    # Filtrame los ingresos cuyo origen coincida con alguna de las cuentas del usuario
    ingresos = Incomes.objects.filter(origen__in=cuentas_bancarias).order_by("-fecha_y_hora")
    context = {
        "ingresos": ingresos,
    }
    return render(request, "income.html", context)


@login_required
def ingresar_dinero(request):
    if request.method == "GET":
        cuentas = BankAccounts.objects.filter(titular=request.user)
        return render(request, "ingresar-dinero.html", {"cuentas": cuentas})
    
    elif request.method == "POST":
        cuenta_sendora = SendoraAccounts.objects.get(titular=request.user)

        cuenta_id = request.POST.get("cuenta")
        monto = request.POST.get("monto")

        # Validamos que los campos estén completos
        if not cuenta_id or not monto:
            return render(request, "ingresar-dinero.html", {
                "mensaje": "Por favor completa todos los campos.",
                "cuentas": BankAccounts.objects.filter(titular=request.user)
            })

        try:
            # Intentamos convertir el monto a Decimal
            monto = monto.strip()  # Eliminamos espacios alrededor
            monto = monto.replace(",", ".")  # Reemplazamos comas por puntos (si es necesario)
            monto = Decimal(monto)  # Convertimos directamente a Decimal
        except (ValueError, InvalidOperation):
            # Si ocurre un error de validación en el monto, mostramos el mensaje
            return render(request, "ingresar-dinero.html", {
                "mensaje_monto_no_valido": "El monto debe ser un número válido.",
                "cuentas": BankAccounts.objects.filter(titular=request.user)
            })

        # Continuamos con el resto de la lógica solo si el monto es válido
        cuenta_bancaria = get_object_or_404(BankAccounts, id=cuenta_id)

        # Verificamos si hay fondos suficientes
        if monto > cuenta_bancaria.saldo:
            return render(request, "ingresar-dinero.html", {
                "mensaje_insuficiente": "Saldo de cuenta bancaria insuficiente",
                "cuentas": BankAccounts.objects.filter(titular=request.user)
            })

        # Si hay saldo suficiente Actualizamos los saldos
        cuenta_bancaria.saldo -= monto
        cuenta_sendora.saldo += monto
        cuenta_bancaria.save()
        cuenta_sendora.save()

        # Registramos el ingreso
        Incomes.objects.create(monto=monto, origen=cuenta_bancaria, destino=SendoraAccounts.objects.get(titular=request.user))

        return render(request, "ingresar-dinero.html", {
            "mensaje_exito": "Ingreso de dinero realizado con éxito.",
            "cuentas": BankAccounts.objects.filter(titular=request.user)
        })
        
@login_required
def ver_ingreso(request, ingreso_id):
    ingreso =  Incomes.objects.get(id=ingreso_id)
    context = {
        "ingreso": ingreso
    }
    return render(request, "comprobante_ingreso.html", context)
     
 