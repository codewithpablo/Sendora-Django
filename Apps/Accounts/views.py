from django.shortcuts import render
from .models import BankAccounts
from django.shortcuts import render, redirect
from .forms import NewBankAccountForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

#!Funcion para listar todas las cuentas bacarias asociadas 
@login_required
def accounts(request):
    usuario_logueado = request.user
    cuentas_bancarias = BankAccounts.objects.filter(titular=usuario_logueado)
    context = {
        "cuentas_bancarias": cuentas_bancarias,
    }
    return render(request, "accounts.html", context)

#!Funcion para añadir  una nueva cuenta bancaria
@login_required
def addbankaccount(request):
    if request.method == 'POST':
        form = NewBankAccountForm(request.POST)
        if form.is_valid():
            # Asignamos el usuario logueado como titular
            
            #Si eliminamos la línea commit=False y tratamos de guardar el formulario directamente con form.save(),
            # voy a obtener  un error porque el campo titular estaría vacío o no tendría un valor válido asignado.
            bank_account = form.save(commit=False) # Esto es necesario para escenarios donde se requiere modificar campos antes de guardar el objeto.
            
            bank_account.titular = request.user  # El titular es el usuario logueado
            bank_account.save() #Ahora si  generame un nuevo registro en la tabla BankAccounts
            return redirect('accounts')  
    else:
        form = NewBankAccountForm()

    return render(request, 'add-account.html', {'form': form})


# @require_POST:
#Si alguien intenta acceder a esta vista usando un método diferente, como GET, 
# Django devolverá automáticamente un error 405 Method Not Allowed, 
# lo que refuerza la seguridad y asegura la semántica HTTP adecuada.

#No necesitamos comprobar manualmente el método de la solicitud
# dentro de la función con if request.method == "POST".

#!Funcion para desvincular(eliminar) una cuenta bancaria asociada
@login_required
@require_POST
def deslink(request, account_id):
    try:
        account = BankAccounts.objects.get(id=account_id)
        account.delete()
        return redirect("accounts") # Redirige a la vista de cuentas
    except BankAccounts.DoesNotExist:
        return redirect("accounts")  # Redirige aunque no exista, evita errores