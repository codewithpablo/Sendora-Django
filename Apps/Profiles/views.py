from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import EditUserForm, EditProfileForm
from django.contrib import messages
from Apps.Profiles.models import Profiles



@login_required
def editprofile(request):
    usuario_logueado = request.user 
    
    #Obtenemos el perfil del usuario logueado
    current_profile = get_object_or_404(Profiles, usuario=usuario_logueado)  
 
    if request.method == "POST":
        
        # Procesamos ambos formularios
        user_form = EditUserForm(request.POST, instance=usuario_logueado)
        profile_form = EditProfileForm(request.POST, request.FILES, instance=current_profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Perfil actualizado exitosamente ✔")
            return redirect("editprofile")  # Redirige a la misma página
        else:
            messages.error(request, "Se ha producido un error, uno de los campos es inválido❌")
            # Depuración para identificar errores
            print("Errores en user_form:", user_form.errors)
            print("Errores en profile_form:", profile_form.errors)
    else:
        # Inicializamos ambos formularios con datos existentes
        user_form = EditUserForm(instance=usuario_logueado)
        profile_form = EditProfileForm(instance=current_profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form,
    }
    return render(request, "editprofile.html", context)
