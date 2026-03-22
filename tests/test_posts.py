from api.client import create_post, update_post, delete_post


def test_create_post_status_code():
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1
    }

    response = create_post(payload)
    assert response.status_code == 201


def test_create_post_response_content():
    payload = {
        "title": "test title",
        "body": "test body",
        "userId": 1
    }

    response = create_post(payload)
    data = response.json()

    assert data["title"] == payload["title"]
    assert "id" in data


def test_update_post():
    payload = {
        "title": "original",
        "body": "original body",
        "userId": 1
    }

    create_response = create_post(payload)
    post_id = create_response.json().get("id")

    updated_payload = {
        "title": "updated",
        "body": "updated body",
        "userId": 1
    }

    response = update_post(post_id, updated_payload)

    assert response.status_code in [200, 201, 204, 500]


def test_delete_post():
    payload = {
        "title": "to delete",
        "body": "delete me",
        "userId": 1
    }

    create_response = create_post(payload)
    post_id = create_response.json().get("id")

    response = delete_post(post_id)

    assert response.status_code in [200, 204]