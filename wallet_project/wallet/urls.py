from django.urls import path
from wallet.views import WalletBalanceView, WalletOperationView

urlpatterns = [
    path('wallets/<uuid:wallet_id>/', WalletBalanceView.as_view(), name='wallet-balance'),
    path('wallets/<uuid:wallet_id>/operation', WalletOperationView.as_view(), name='wallet-operation'),
]
