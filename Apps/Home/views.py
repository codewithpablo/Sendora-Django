from django.shortcuts import render, redirect


# Funcion 1
def home(request):
    if request.user.is_authenticated:
        # Redirige a la vista de pacientes si el usuario ya está autenticado
        return redirect('dashboard')
    return render(request, "home.html")

def redirect_to_home(request):
    return redirect("home")