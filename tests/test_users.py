import pytest
from api.client import get_users


def test_get_users_status_code():
    response = get_users()
    assert response.status_code == 200


def test_users_not_empty(users):
    assert len(users) > 0


def test_user_has_email(users):
    for user in users:
        assert "email" in user
        assert "@" in user["email"]


@pytest.mark.parametrize("user_index", [0, 1, 2])
def test_users_have_valid_email(user_index, users):
    user = users[user_index]
    email = user["email"]

    assert email is not None
    assert "@" in email
