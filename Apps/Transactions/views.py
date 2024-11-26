from django.shortcuts import render, redirect
from Apps.Transactions.models import Transactions
from .models import Transactions
from Apps.Accounts.models import SendoraAccounts
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from Apps.Motives.models import Motives
from Apps.Profiles.models import Profiles
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from Apps.Users.models import Users
from django.db.models import Q

#!Funcion para ver todas las transacciones enviadas y recibidas
@login_required
def transactions(request):
    usuario = request.user
    
    # Filtrame las transacciones donde el usuario es el remitente o el destinatario
    entradas = Transactions.objects.filter(destinatario = usuario).order_by('-fecha_y_hora')
    salidas = Transactions.objects.filter(remitente = usuario).order_by('-fecha_y_hora')
    
    context = {
        'entradas': entradas,
        'salidas': salidas,
        
        }
    return render(request, "transactions.html", context)


#! Funcion para marcar como favorita a una cuenta Sendora
@login_required
def marcar_favorita(request, account_id):
    # Obteneiendo la cuenta Sendora a ser marcada como favorita
    cuenta = get_object_or_404(SendoraAccounts, id=account_id)
    
    # Obteniendo el perfil actual (del usuario logueado)
    perfil, created = Profiles.objects.get_or_create(usuario=request.user)
    
    # Verificamos si la cuenta ya está marcada como favorita
    if cuenta in perfil.cuentas_favoritas.all():
        # Si ya está en favoritos, desmárcala
        perfil.cuentas_favoritas.remove(cuenta)
    else:
        # Si no está en favoritos, agrégala
        perfil.cuentas_favoritas.add(cuenta)

    # Redirigime a la lista de transacciones
    return redirect('vercontactos')


#! Funcion para enviar dinero a otra cuenta
@csrf_exempt  # Desactiva la protección CSRF 
@require_http_methods(["GET", "POST"])  # Acepta solo métodos GET y POST
@login_required
def realizar_transferencia(request):
    if request.method == "GET":
        
        context = {
            "usuarios_favoritos": Profiles.objects.get(usuario = request.user).cuentas_favoritas.all(),
            "motivos": Motives.objects.all()
        }
        # Renderizame el formulario para realizar la transferencia
        return render(request, "make-transaction.html", context)  

    if request.method == "POST":
        # Extrayanedo los datos del formulario
        alias_destino = request.POST.get('alias_destino')
        motivo_nombre = request.POST.get("motivo")
        monto = int(request.POST.get('monto')) # Convertmos a int, pero, por que es esto necesario? Explicacion abajo
        
        # el valor que se obtiene de request.POST.get('monto') es siempre una cadena (string), incluso si el usuario introduce un número en el formulario.
        # En otras palabras, cuando un usuario envía un formulario en HTML, 
        # los datos son enviados como texto (strings), independientemente de que el campo sea un número.

        # Si no te pasan un monto o el alias, devolve un mensaje
        if not alias_destino or not monto:
            context = {
                 "motivos": Motives.objects.all(),
                "mensaje_incompletos": "Campos de texto incompletos" 
            }
            return render(request, "make-transaction.html", context)
        
        if monto <= 0:
            context = {
             "motivos": Motives.objects.all(),
            "mensaje_numero_positivo": "El monto no puede ser menor a 0" 
            }
            return render(request, "make-transaction.html", context)
            
        
        try:
            # Obteniendo cuentas bancairas desde la base de datos
            cuenta_origen = SendoraAccounts.objects.get(titular=request.user)
            cuenta_destino = SendoraAccounts.objects.get(alias=alias_destino)
            
            # Verificando si el saldo es suficiente, si no lo es corta la funcion y devolve un mensaje
            if cuenta_origen.saldo < float(monto):
                    context = {
                    "mensaje_insuficiente": "Su saldo es insuficiente" 
                    }
                    return render(request, "make-transaction.html", context)
            
            # Si el saldo es suficiente, hace la transfernecia
            cuenta_origen.transferir(cuenta_destino, monto)
            
            # Obtener o crear el motivo
            motivo_objeto, seCreo = Motives.objects.get_or_create(nombre=motivo_nombre)

            #Voy a registrar la transaccion
            Transactions.objects.create(monto=monto, remitente=request.user, destinatario=cuenta_destino.titular, motivo=motivo_objeto)
            
            # Respuesta exitosa
            context = {
                "mensaje_exito": "Transferencia realizada con exito" 
            }
            
            #Renderizo el formulario con un mensaje de exito
            return render(request, "make-transaction.html", context)
        except SendoraAccounts.DoesNotExist:
            
            context = {
                "motivos": Motives.objects.all(),
                "mensaje_no_existe": "El alias especificado no existe" 
            }
            return render(request, "make-transaction.html", context)
        
#! Funcion para borrar transacciones
@login_required
def borrar_transacciones(request):
    pass

#! Funcion para ver comprobante
@login_required
def ver_comprobante(request, id_comprobante):
    transaccion = Transactions.objects.get(id=id_comprobante)
    context = {
        "transaccion": transaccion
    }
    return render(request, "comprobante.html", context)


def contacts(request):
    # Filtrame los usuarios que yo les envie dinero, y todos aquellos des lo que recibi dinero
    contactos = Users.objects.filter(
        Q(id__in=Transactions.objects.filter(remitente=request.user).values('destinatario')) | 
        Q(id__in=Transactions.objects.filter(destinatario=request.user).values('remitente'))
    )
    context = {
        "contactos": contactos
    }
    
    return render(request, "contacts.html", context)


"""
Si Mark Zuckerberg, por ejemplo, cumple con alguna de las dos condiciones 
(por ejemplo, si te envió dinero o si tú le enviaste dinero), entonces esa transacción 
se aplicaría para él en el conjunto de resultados. Como estás usando OR (condición compuesta),
si alguna de las condiciones es verdadera para él, su perfil será incluido en el conjunto de contactos.
"""
