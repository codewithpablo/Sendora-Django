**BREVE DESCRIPCION DEL PROYECTO**

Sendora es un proyecto hecho con Django y Taiwlind CSS

El objetivo de este sitio web es que los usuarios puedan gestionar sus movimientos financieros.

Sendora posee 4 tipos de funcionalidades principales:

1) Funcionalidades generales:
    -Iniciar sesion
    -Crear cuenta nueva

2) Funcionalidades para usuarios clientes:
    -Transferir dinero
    -Ingresar dinero
    -Recibir dinero
    -Editar perfil propio
    -Ver comprobante de cada movimineto financiero
    -Ver historial de transacciones recientes e historial completo
    -Ver historial de ingresos a su propia cuenta Sendora

3) Funcionalidades para usuarios administradores
    -Editar, leer, crear y borrar un motivo de transferencia
    -Ver lista de usurios, editarlos y activarlos/desactivarlos
    -Ver todas las cuentas Sendora y consultar sus movimientos

4) Funcionalidades Extra
    -Asociar y desvincular cuentas bancarias 
    -Visualizar el monto total acumulado entre todas las cuentas bancarias asociadas

**INTEGRANTES**
Desarrollado de forma individual por Alonso, Pablo


**ACLARACIONES ADICIONALES**

En el Project/settings.py:

# Configuración de archivos multimedia
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# URL de inicio de sesión
LOGIN_URL=/login/

# Configuración del modelo de usuario
AUTH_USER_MODEL=Users.Users

# Procesadores propios
'processors.profile.get_profile', 
'processors.es_administrador.usuario_es_administrador'

# Aplicaiones añadidas
    'Apps.Auth',
    'Apps.Home',
    'Apps.Banks',
    'Apps.Transactions',
    'Apps.Dashboard',
    'Apps.Users.apps.UsersConfig', 
    'Apps.Accounts',
    'Apps.Income',
    'Apps.Profiles',
    'Apps.Motives',
    'Apps.Cards',
    'Apps.Admin',
    'tailwind',
     'theme',
     'django_browser_reload',
     'django.contrib.humanize'







