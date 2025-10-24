import pytest

# POST /posts с валидными данными
@pytest.mark.post_vaid
def test_create_post(api_client):
    post=api_client.create_post("zagolovok","test_body","12")
    assert post is not None
    assert post['title'] == "zagolovok"
    assert post['body'] == "test_body"
    assert post['id'] == "12"

# ответ содержит id, title, body, userId
@pytest.mark.field_valid
def test_create_post_field_valid(api_client):
    post=api_client.create_post("zagolovok","test_body","12")
    assert post is not None
    assert post['title'] == "zagolovok"
    assert post['body'] == "test_body"
    assert post['id'] == "12"

# статус-код = 201
@pytest.mark.post
def test_create_post_status(api_client):
    post=api_client.create_post("zagolovok","body","12")
    assert post.status == 201
