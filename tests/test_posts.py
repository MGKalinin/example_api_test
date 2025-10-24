import pytest
import requests

@pytest.mark.post_valid
def test_create_post(api_client):
    """Тест: создание поста с валидными данными."""
    post = api_client.create_post("zagolovok", "test_body", 12)
    assert post is not None
    assert post["title"] == "zagolovok"
    assert post["body"] == "test_body"
    assert post["userId"] == 12  # переданный user_id
    assert "id" in post  # id генерируется сервером, проверяем только наличие


@pytest.mark.field_valid
def test_create_post_field_valid(api_client):
    """Тест: ответ содержит все обязательные поля."""
    post = api_client.create_post("zagolovok", "test_body", 12)
    assert post is not None
    required_fields = {"id", "title", "body", "userId"}
    assert required_fields.issubset(post.keys())


@pytest.mark.post
def test_create_post_returns_201_status(api_client):
    """Тест: POST /posts возвращает статус 201."""
    # Так как текущий APIClient не возвращает статус,
    # выполним запрос напрямую для проверки статуса
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        json={"title": "temp", "body": "temp", "userId": 1}
    )
    assert response.status_code == 201