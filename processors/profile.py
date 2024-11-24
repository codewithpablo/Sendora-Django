from django.contrib.auth.models import AnonymousUser
from Apps.Profiles.models import Profiles
from django.shortcuts import redirect

def get_profile(request):
    # Verifica si el usuario está autenticado
    if isinstance(request.user, AnonymousUser):
        return {}  # Devuelve un diccionario vacío si el usuario no está autenticado
    
    try:
        # Si el usuario está autenticado, intenta obtener su perfil
        perfil = Profiles.objects.get(usuario=request.user)
    except Profiles.DoesNotExist:
        perfil = None  # Si el perfil no existe, maneja el caso
    
    # Siempre devuelves un diccionario válido
    return {
        'perfil': perfil if perfil else None
    }
