from django.urls import path
from .views import UsersListView, toggle_user_active, MotivesListView, SendoraAccountsListView, MotivesCreateView, MotivesDeleteView, MotivesUpdateView, MovimientosView, UsuarioUpdateView

urlpatterns = [
    
    #Usuarios
    path("lista_de_usuarios/", UsersListView.as_view(), name="lista_de_usuarios"),
    path("edicion_de_usuarios/<int:pk>/", UsuarioUpdateView.as_view(), name="ediciondeusuario"),
    
    #Motivos
    path("lista_de_motivos/", MotivesListView.as_view(), name="lista_de_motivos"),
    path("crear_nuevo_motivo/", MotivesCreateView.as_view(), name="crearmotivo"),
    path("eliminar_motivo/<int:pk>/", MotivesDeleteView.as_view(), name="eliminarmotivo"), #El parametro que le paso debe llamarse pk, sino no funciona. Por otro, ladoDeleteView hereda de BaseDeleteView, y esta clase utiliza el identificador que las paso por URL para buscar y eliminar el objeto.
    path("editar_motivo/<int:pk>/", MotivesUpdateView.as_view(), name="editarmotivo"), 
    
    #Cuentas Sendora
    path("lista_de_cuentas/", SendoraAccountsListView.as_view(), name="lista_de_cuentas"),
     path('toggle_user_active/<int:user_id>/', toggle_user_active, name='toggle_user_active'),
     
     #Movimientos
     path('movimientos/<int:pk>/', MovimientosView.as_view(), name='movimientos'),
]
