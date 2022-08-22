import pytest
from factories import MovieFactory
from rest_framework.test import APIClient


@pytest.fixture()
def client_api():
    client = APIClient()
    return client
