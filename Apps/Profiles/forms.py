from Apps.Users.models import Users
from django import forms
from Apps.Profiles.models import Profiles

#Cuando el usuario modifica su informacion, lo que esta haciendo es modificar 2 tablas: la de usuarios y la de perfil

#Formulario de edicion de campos que pertenence al modelo usuario
class EditUserForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['username','first_name', 'last_name', 'email', ]

        
#Formulario de edicion de campos que pertenecen al modelo Perfil
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profiles
        fields = ['foto_perfil', 'dni', 'phone_number', 'fecha_nacimiento', ]  