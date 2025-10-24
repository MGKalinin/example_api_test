import pytest

# users возвращает список из 10 пользователей
@pytest.mark.ten_users
def test_ten_users(api_client):
    users=api_client.get_users()
    assert len(users)==10

# у каждого пользователя есть поля: id, name, email
@pytest.mark.set
@pytest.mark.parametrize(
    "fields",
    [
        pytest.param("id", id="field: id"),
        pytest.param("name", id="field: name"),
        pytest.param("email", id="field: email"),
    ],
)
def test_parametrized_fields(api_client, fields):
    users=api_client.get_users()
    for user in users:
        assert fields in user, f"Поле '{fields}' отсутствует у пользователя {user.get('id', 'unknown')}"

# GET /users/1 возвращает пользователя с id == 1
@pytest.mark.users1
def test_user1(api_client):
    user=api_client.get_user(user_id=1)
    assert user is not None ,"Пользователь не найден"
    assert user['id'] == 1

