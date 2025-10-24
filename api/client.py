import requests

class APIClient:
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self,user_id=None,title=None,body=None):
        self.user_id=user_id
        self.title=title
        self.body=body

    def get_users(self):
        """Метод возвращает список пользователей"""
        url = f"{self.BASE_URL}/users"
        response = requests.get(url)
        response.raise_for_status()  # выбросит исключение при ошибке HTTP
        return response.json()

    def get_user(self,user_id):
        """Метод возвращает данные конкретного пользователя"""
        url = f"{self.BASE_URL}/users/{user_id}"
        response = requests.get(url)
        if response.status_code == 404:
            print(f"Пользователь с id={user_id} не найден.")
            return None
        response.raise_for_status()
        return response.json()

    def create_post(self,title, body, user_id):
        """Метод создаёт пост (возвращает созданный объект с id)"""
        url = f"{self.BASE_URL}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json()

example=APIClient()
print(example.create_post("zagolovok","body","12"))

