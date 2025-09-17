# Wallet API

API-сервис для работы с кошельками: пополнение, вывод средств и получение баланса.  
Проект разработан с использованием Django, PostgreSQL, DRF, полностью контейнеризирован с помощью **Docker** и покрыт тестами.

---

## Cтруктура проекта

<img width="629" height="826" alt="image" src="https://github.com/user-attachments/assets/a43ff217-de6c-4f9a-ac41-f9c869b2027e" />


##  Быстрый старт

1. Клонируйте репозиторий:
   git clone https://github.com/your-username/wallet-api.git
   cd wallet-api
2. Запустите проект(у вас должен быть установлен докер):
   docker-compose up --build
3. Перейди по адресу:
    API: http://localhost:8000/api/v1/wallets/UUID/
    Тестовые UUID 347f9357-19cb-4ff2-96db-85b5db287793, 25c0891e-e754-4439-b865-b0dabe3dda45
    Админка: http://localhost:8000/admin/
   
##  Технологии
  Python	✅ v3.11
  Django	✅ v5.2+
  PostgreSQL	✅ v15
  DRF (Django REST)	✅
  Docker & Compose	✅
  Unittest	✅


## Доступ в админку

  Адрес: http://localhost:8000/admin/
  Логин: root
  Пароль: 1
  Либо вы можете создать сами, выполнив команду в терминале
  docker-compose exec web python manage.py createsuperuser

  
## Тесты
 
  
  Протестированы следующие случаи:
  
  ✅ Пополнение средств
  ✅ Снятие средств (успешное и при недостатке баланса)
  ✅ Неверный тип операции
  ✅ Получение баланса
  
  Запуск тестов:
  docker-compose exec web python manage.py test wallet.tests
  ✅ Логи тестов сохраняются в файл test_results.log
  ✅ Также проводится логгирование всех операций внутри tests.py

## Скриншоты

Успешный POST-запрос (DEPOSIT)
<img width="825" height="569" alt="image" src="https://github.com/user-attachments/assets/73a8422e-5150-4354-ac5a-09711af67995" />


Ошибка при недостатке средств
<img width="842" height="570" alt="image" src="https://github.com/user-attachments/assets/daf396f2-f888-43b3-b30f-526190ab4986" />


Получение баланса
<img width="817" height="540" alt="image" src="https://github.com/user-attachments/assets/51387f53-7090-4204-bc5e-ff2ae7eb3e52" />

## Комментарий. 
  Я понимаю, что данную работу можно еще развивать. Как минимум тесты я сделал примитивные и не обработал еще случаи, что касается снятия и пополнения.
  Прекрасно понимаю, что это минимум от всей необходимой работы
