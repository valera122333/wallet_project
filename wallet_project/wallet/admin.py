from django.contrib import admin
from .models import Wallet, Operation

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('id', 'balance')

@admin.register(Operation)
class OperationAdmin(admin.ModelAdmin):
    list_display = ('id', 'wallet', 'operation_type', 'amount', 'created_at')
    list_filter = ('operation_type',)
