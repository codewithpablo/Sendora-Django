from django import forms
from .models import Incomes

class IngresarDineroForm(forms.ModelForm):
    
    class Meta:
        model = Incomes
        fields = ["monto", "origen"]
    
    