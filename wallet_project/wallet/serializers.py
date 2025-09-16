from rest_framework import serializers
from .models import Wallet, Operation

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('operation_type', 'amount')

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'balance')
