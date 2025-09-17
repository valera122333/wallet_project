import uuid
from django.db import models
from django.db import transaction
from django.core.exceptions import ValidationError

class Wallet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)

class Operation(models.Model):
    DEPOSIT = 'DEPOSIT'
    WITHDRAW = 'WITHDRAW'
    OPERATION_CHOICES = [
        (DEPOSIT, 'Deposit'),
        (WITHDRAW, 'Withdraw'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='operations')
    operation_type = models.CharField(max_length=10, choices=OPERATION_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.amount <= 0:
            raise ValidationError("Сумма должна быть положительным числом")
    
        with transaction.atomic():
            wallet = Wallet.objects.select_for_update().get(pk=self.wallet.pk)
            if self.operation_type == self.DEPOSIT:
                wallet.balance += self.amount
            elif self.operation_type == self.WITHDRAW:
                if wallet.balance < self.amount:
                    raise ValueError("Недостаточно средств")
                wallet.balance -= self.amount
            wallet.save()
            super().save(*args, **kwargs)

 