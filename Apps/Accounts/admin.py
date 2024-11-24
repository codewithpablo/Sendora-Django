from django.contrib import admin
from .models import BankAccounts, SendoraAccounts, CorporateAccounts




# Registro para BankAccounts
@admin.register(BankAccounts)
class BankAccountsAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de BankAccounts
    list_display = ('id', 'alias', 'titular', 'banco', 'saldo')
    
    # Campos que serán utilizables para buscar en el admin
    search_fields = ('alias', 'titular__username', 'banco__nombre')  # Ajusta según el nombre de los campos en el modelo Users y Banks
    
    # Filtros disponibles en la barra lateral
    list_filter = ('titular', 'banco', 'saldo')




# Registro para SendoraAccounts
@admin.register(SendoraAccounts)
class SendoraAccountsAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de SendoraAccounts
    list_display = ('id', 'alias', 'titular', 'saldo')
    
    # Campos que serán utilizables para buscar en el admin
    search_fields = ('alias', 'titular__username',)  # Ajusta según los campos de relación
    
    # Filtros disponibles en la barra lateral
    list_filter = ('titular', 'saldo')




# Registro para SendoraAccounts
@admin.register(CorporateAccounts)
class CorporateAccountsAdmin(admin.ModelAdmin):
    # Campos que se mostrarán en la lista de SendoraAccounts
    list_display = ('id', 'alias', 'titular', 'banco', 'saldo')
    
    # Campos que serán utilizables para buscar en el admin
    search_fields = ('alias', 'titular__username', 'banco__alias')  # Ajusta según los campos de relación
    
    # Filtros disponibles en la barra lateral
    list_filter = ('titular', 'banco', 'saldo')
