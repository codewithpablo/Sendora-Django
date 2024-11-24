from django import forms
from .models import BankAccounts


class NewBankAccountForm(forms.ModelForm):
    
       
    class Meta:
        model = BankAccounts
        fields = ['alias', 'banco']
        
        
       
