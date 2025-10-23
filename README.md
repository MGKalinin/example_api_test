# example_api_test   
🧪 Тестовое задание: Автоматизированные тесты на Python + PyTest
🎯 Цель
Разработать небольшой фреймворк автоматизированных тестов для REST API с использованием Python и PyTest.

📦 Что дано
Публичное демо-API: https://jsonplaceholder.typicode.com
(Это бесплатный mock-сервис для тестирования REST API)

Нас интересуют эндпоинты:

GET /users — список пользователей   
GET /users/{id} — данные конкретного пользователя   
POST /posts — создание поста (возвращает созданный объект с id)   
✅ Задачи   
### 1.Создайте структуру проекта:   
```angular2html
autotest_project/
├── tests/
│   ├── test_users.py
│   └── test_posts.py
├── api/
│   └── client.py
├── conftest.py
└── requirements.txt
```
### 2.Напишите API-клиент (api/client.py):   
Класс APIClient с методами:   
get_users() → list   
get_user(user_id) → dict   
create_post(title, body, user_id) → dict   
Используйте библиотеку requests
Обрабатывайте HTTP-ошибки (минимум через raise_for_status())   
### 3.Напишите тесты на PyTest:   
В test_users.py:
Проверить, что /users возвращает список из 10 пользователей   
Проверить, что у каждого пользователя есть поля: id, name, email   
Проверить, что GET /users/1 возвращает пользователя с id == 1   
В test_posts.py:   
Отправить POST /posts с валидными данными   
Проверить, что ответ содержит id, title, body, userId   
Проверить, что статус-код = 201   
### 4.Используйте фикстуры (conftest.py):   
Создайте фикстуру api_client, которая возвращает экземпляр APIClient
Используйте её в тестах через параметр   
### 5.Добавьте параметризацию (опционально, но плюсом):   
Протестируйте несколько user_id (1, 2, 3) в одном тесте через @pytest.mark.parametrize   
### 6.requirements.txt:   
Укажите зависимости:
```
requests==2.32.3
pytest==8.3.3
```
📌 Требования к качеству кода
Соблюдайте PEP8
Используйте понятные имена функций/переменных
Тесты должны быть независимыми и идемпотентными
Не используйте time.sleep() — только явные проверки   

1.Добавь файлы в коммит   
```angular2html
git add .
```   
2.Проверь:
```angular2html
git status
```   
Ты должен увидеть все новые файлы в зелёном цвете.   
3.Сделай коммит  
```angular2html
git commit -m "Добавил файлы проекта и обновил README"
```   
4.Отправь изменения в GitHub   
```angular2html
git push origin main
```