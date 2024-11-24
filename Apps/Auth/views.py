from django.shortcuts import render, redirect
from django.contrib.auth.forms  import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib import messages
from Apps.Accounts.models import SendoraAccounts


# Funcion 2
def log_in(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("dashboard")
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
    else:
        user = authenticate(request, username=request.POST["username"], password=request.POST["password"])
        print(request.POST["username"], request.POST["password"])
        if user is None:
            form = AuthenticationForm()
            messages.error(request, "Ocurrió un error al autenticar al usuario!")
            return render(request, "login.html", {"form": form })
        else:
            login(request, user)
            return redirect('dashboard')

# Funcion 3
@login_required
def log_out(request):
    logout(request)
    return redirect("home")

# Funcion 4
def sign_up(request):
    
    #Cuando ingresamos a la pagina para poder registrarnos
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("dashboard")
        form = SignUpForm()
        return render(request, "signup.html", {"form": form})
    
    #Cuando hacemos click en el boton de enviar los datos
    else:
        form = SignUpForm(request.POST)
        if form.is_valid():  # Se el formulario es valido (incluyendo si las contraseñas coinciden)
                # Creamos el usuario usando el formulario
                user = form.save()
                
                # Iniciamos sesión automáticamente
                login(request, user)
                
                #Automatimcamente despues de que se cree un nuevo usuario, se le crea una cuenta Sendora
                SendoraAccounts.objects.create(alias=request.user.username, titular=request.user)
           
                # Redireccionmosa a la lista de pacientes
                return redirect('dashboard')
        else:
            # Si el formulario no es válido (contraseñas no coinciden, nombre de usuario ya existente, contraseña muy corta/comun/simple, etc)
            return render(request, "signup.html", {"form": form } )
        
        
