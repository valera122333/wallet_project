from rest_framework import serializers
from .models import Wallet, Operation

class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = ('operation_type', 'amount')
    
        def validate_amount(self, value):
            if value <= 0:
                raise serializers.ValidationError("Сумма должна быть больше нуля.")
            return value

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ('id', 'balance')
