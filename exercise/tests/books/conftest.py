import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def client_api():
    client = APIClient()
    return client


@pytest.fixture
def gutendex_example_1():
    return {}


@pytest.fixture
def gutendex_example_2():
    return {
        
    }


@pytest.fixture()
def gutendex_search_data(gutendex_example_1, gutendex_example_2):
    return {
        "count": 2,
        "next": None,
        "previous": None,
        "results": [gutendex_example_1, gutendex_example_2],
    }
