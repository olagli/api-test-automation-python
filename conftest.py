import pytest
from api.client import get_users


@pytest.fixture
def users():
    response = get_users()
    return response.json()