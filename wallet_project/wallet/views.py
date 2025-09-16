from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Wallet, Operation
from .serializers import OperationSerializer, WalletSerializer
from django.shortcuts import get_object_or_404

class WalletBalanceView(APIView):
    def get(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        serializer = WalletSerializer(wallet)
        return Response(serializer.data)

class WalletOperationView(APIView):
    def post(self, request, wallet_id):
        wallet = get_object_or_404(Wallet, id=wallet_id)
        serializer = OperationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            operation = Operation(wallet=wallet, **serializer.validated_data)
            operation.save()
        except ValueError as e:
            return Response({'detail': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'detail': 'Operation successful'}, status=status.HTTP_200_OK)
