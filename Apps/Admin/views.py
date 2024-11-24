from Apps.Users.models import Users
from Apps.Transactions.models import Transactions
from Apps.Income.models import Incomes
from Apps.Motives.models import Motives
from Apps.Accounts.models import SendoraAccounts
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import NuevoMotivoForm
from Apps.Accounts.models import SendoraAccounts
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.db.models import Q

#! Usuarios (Read, Update)
class UsersListView(ListView):
    model = Users
    template_name = "usuarios/list-of-users.html"
    
    
def toggle_user_active(request, user_id):
    # Obteneme el usuario basado en el ID que te pasan por parametro
    usuario = get_object_or_404(Users, id=user_id)
    # Cambiame el estado del usuario
    usuario.is_active = not usuario.is_active
    usuario.save()
    # Redirigime de vuelta a la lista de usuarios 
    return redirect('lista_de_usuarios')  


class UsuarioUpdateView(UpdateView):
    model = Users
    fields = ['first_name', 'last_name', 'email']  # Campos que se pueden editar
    template_name = 'usuarios/edicion-usuario.html'
    success_url = reverse_lazy('lista_de_usuarios')

    def get_context_data(self, **kwargs):
        # Llamamos al método de la clase base para obtener el contexto
        context = super().get_context_data(**kwargs)

        # Agregamos información adicional al contexto, por ejemplo, el usuario actualizado
        usuario = self.get_object()  # Obtiene el objeto del usuario actual
        context['usuario'] = usuario

        # Puedes agregar más variables de contexto aquí si es necesario
        return context

    

#! Cuentas (Read)
class SendoraAccountsListView(ListView):
    model = SendoraAccounts
    template_name = "cuentas/list-of-accounts.html"

#! Movimientos (Read)
class MovimientosView(ListView):
    template_name = 'movimientos/movimientos.html'

    def get_queryset(self):
        return []  # No se usa queryset base, ya que personalizaremos el contexto.

    def get_context_data(self, **kwargs):
        # Llamar al método base para obtener el contexto inicial
        context = super().get_context_data(**kwargs)

        # Obtener el pk desde la URL
        pk = self.kwargs['pk']

        # Obtener el usuario usando el pk
        usuario = get_object_or_404(Users, id=pk)

        # Filtrar transacciones donde el usuario sea remitente o destinatario
        context['transacciones'] = Transactions.objects.filter(
            Q(remitente=usuario) | Q(destinatario=usuario)
        )

        # Obtener la cuenta Sendora del usuario
        sendora_account = get_object_or_404(SendoraAccounts, titular=usuario)
        print(sendora_account.id)

        # Filtrar los ingresos hacia la cuenta Sendora
        context['ingresos'] = Incomes.objects.filter(destino=sendora_account)

        # Imprimir información para depurar
        print("Usuario:", usuario)
        print("Sendora Account:", sendora_account)
        print("Ingresos encontrados:", context['ingresos'])

        # Añadir el usuario al contexto (opcional)
        context['usuario'] = usuario

        return context

    
    
#! Motivos (CRUD)

class MotivesListView(ListView):
    model = Motives
    template_name = "motivos/list-of-motives.html"

class MotivesCreateView(CreateView):
    model = Motives
    form_class = NuevoMotivoForm
    template_name = "motivos/agregar-motivo.html"
    success_url = reverse_lazy("lista_de_motivos")
    
    def get_context_data(self, **kwargs): #Esto asegura que el contexto básico con los datos del modelo esté presente.
        context = super().get_context_data(**kwargs)
         # Agrego datos adicionales al contexto
        context['title'] = 'Crear motivo'

class MotivesDeleteView(DeleteView):
    model = Motives  # Modelo que quieres eliminar
    success_url = reverse_lazy("lista_de_motivos")



class MotivesUpdateView(UpdateView):
    model = Motives
    fields = ['nombre']  # Campos que se pueden editar
    template_name = 'motivos/editar-motivo.html'  
    success_url = reverse_lazy('lista_de_motivos')  
    

