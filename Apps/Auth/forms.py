from django import forms
from Apps.Users.models import Users
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):

        
    class Meta:
        model = Users
        fields = ['username','first_name', 'last_name', 'email']
       

      
