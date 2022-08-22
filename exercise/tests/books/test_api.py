from datetime import datetime
from unittest import mock

import pytest
from django.urls import reverse
from factories import ReviewFactory


# @mock.patch("books.client.GutendexClient.search")
# def test_gutendex_search_book_by_title_should_retrieve_list_of_books(
#     client_search_mock, client_api, gutendex_search_data
# ):
#     client_search_mock.return_value = gutendex_search_data

#     url = "{}?{}".format(reverse("books:book-list"), "search=foo")
#     response = client_api.get(url, format="json")
#     assert response.status_code == 200
#     assert len(response.data) == 2


