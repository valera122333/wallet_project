import logging
import uuid
from django.test import TestCase
from django.urls import reverse
from wallet.models import Wallet

#логирование тестов
logger = logging.getLogger('wallet_tests')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('test_results.log', mode='w')
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

class WalletAPITestCase(TestCase):
    def setUp(self):
        self.wallet = Wallet.objects.create()
        self.balance_url = reverse('wallet-balance', kwargs={'wallet_id': self.wallet.id})
        self.operation_url = reverse('wallet-operation', kwargs={'wallet_id': self.wallet.id})
        logger.info(f"Создан кошелек с ID {self.wallet.id} и начальный баланс =  {self.wallet.balance}")

    def test_deposit_operation(self):
        deposit_data = {"operation_type": "DEPOSIT", "amount": "1000"}
        logger.info(f"Тестовая операция DEPOSIT с данными: {deposit_data}")
        response = self.client.post(self.operation_url, deposit_data, content_type='application/json')
        self.wallet.refresh_from_db()
        logger.info(f"Статус: {response.status_code},Баланс кошелька после пополнения: {self.wallet.balance}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(self.wallet.balance), 1000)

    def test_withdraw_operation_success(self):
        self.wallet.balance = 1000
        self.wallet.save()
        withdraw_data = {"operation_type": "WITHDRAW", "amount": "500"}
        logger.info(f"Тестовая операция ВЫВОДА с данными: {withdraw_data}, начальный баланс: {self.wallet.balance}")
        response = self.client.post(self.operation_url, withdraw_data, content_type='application/json')
        self.wallet.refresh_from_db()
        logger.info(f"Статус: {response.status_code}, баланс после снятия: {self.wallet.balance}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(self.wallet.balance), 500)

    def test_withdraw_operation_insufficient_funds(self):
        self.wallet.balance = 100
        self.wallet.save()
        withdraw_data = {"operation_type": "WITHDRAW", "amount": "200"}
        logger.info(f"Тестовая операция ВЫВОДА средств при недостаточном количестве средств: {withdraw_data}, баланс: {self.wallet.balance}")
        response = self.client.post(self.operation_url, withdraw_data, content_type='application/json')
        self.wallet.refresh_from_db()
        logger.info(f"Статус: {response.status_code}, Баланс кошелька после неудачного вывода: {self.wallet.balance}")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(float(self.wallet.balance), 100)

    def test_invalid_operation_type(self):
        invalid_data = {"operation_type": "INVALID", "amount": "100"}
        logger.info(f"Пример неверной операции: {invalid_data}")
        response = self.client.post(self.operation_url, invalid_data, content_type='application/json')
        logger.info(f"Статус: {response.status_code}")
        self.assertEqual(response.status_code, 400)

    def test_get_wallet_balance(self):
        self.wallet.balance = 1234.56
        self.wallet.save()
        logger.info(f"Тест баланса кошелька GET, идентификатор кошелька: {self.wallet.id}, баланс: {self.wallet.balance}")
        response = self.client.get(self.balance_url)
        logger.info(f"Статус: {response.status_code}, : {response.json()}")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(float(response.json()['balance']), 1234.56)
    
    def test_negative_deposit(self):
        data = {"operation_type": "DEPOSIT", "amount": "-100"}
        response = self.client.post(self.operation_url, data, content_type='application/json')
        self.assertEqual(response.status_code, 400)
