from datetime import datetime
from unittest import mock

import pytest
from django.urls import reverse
from factories import MovieFactory


@pytest.mark.django_db()
def test__retrieve_same_produce_max_and_min_result(client_api):
    MovieFactory(year=1980)
    MovieFactory(year=1990)
    MovieFactory(year=2001)

    url = reverse("movie:movie-stats-list")
    response = client_api.get(url, format="json")

    assert response.status_code == 200
    assert response.data["min"][0]["producer"] == "Jerry Weintraub"
    assert response.data["min"][0]["interval"] == 10
    assert response.data["min"][0]["previousWin"] == 1980
    assert response.data["min"][0]["followingWin"] == 1990

    assert response.data["max"][0]["producer"] == "Jerry Weintraub"
    assert response.data["max"][0]["interval"] == 11
    assert response.data["max"][0]["previousWin"] == 1990
    assert response.data["max"][0]["followingWin"] == 2001


@pytest.mark.django_db()
def test__retrieve_different_produce_max_and_min_result(client_api):

    MovieFactory(year=1980)
    MovieFactory(year=1982)
    MovieFactory(producer="Allan", year=1920)
    MovieFactory(producer="Allan", year=1950)

    url = reverse("movie:movie-stats-list")
    response = client_api.get(url, format="json")

    assert response.status_code == 200
    assert response.data["min"][0]["producer"] == "Jerry Weintraub"
    assert response.data["min"][0]["interval"] == 2
    assert response.data["min"][0]["previousWin"] == 1980
    assert response.data["min"][0]["followingWin"] == 1982

    assert response.data["max"][0]["producer"] == "Allan"
    assert response.data["max"][0]["interval"] == 30
    assert response.data["max"][0]["previousWin"] == 1920
    assert response.data["max"][0]["followingWin"] == 1950


@pytest.mark.django_db()
def test__retrieve_different_produce_with_same_dates_max_and_min_result(client_api):

    MovieFactory(year=1980)
    MovieFactory(year=1982)
    MovieFactory(producer="Allan", year=1980)
    MovieFactory(producer="Allan", year=1982)

    url = reverse("movie:movie-stats-list")
    response = client_api.get(url, format="json")

    assert response.status_code == 200
    assert response.data["min"][0]["producer"] == "Allan"
    assert response.data["min"][0]["interval"] == 2
    assert response.data["min"][0]["previousWin"] == 1980
    assert response.data["min"][0]["followingWin"] == 1982

    assert response.data["min"][1]["producer"] == "Jerry Weintraub"
    assert response.data["min"][1]["interval"] == 2
    assert response.data["min"][1]["previousWin"] == 1980
    assert response.data["min"][1]["followingWin"] == 1982

    assert response.data["max"][0]["producer"] == "Allan"
    assert response.data["max"][0]["interval"] == 2
    assert response.data["max"][0]["previousWin"] == 1980
    assert response.data["max"][0]["followingWin"] == 1982

    assert response.data["max"][1]["producer"] == "Jerry Weintraub"
    assert response.data["max"][1]["interval"] == 2
    assert response.data["max"][1]["previousWin"] == 1980
    assert response.data["max"][1]["followingWin"] == 1982


@pytest.mark.django_db()
def test__create_movie(client_api):

    content_data = {
        "producer": "Test 1",
        "title": "Title name",
        "studio": "Studio 1",
        "winner": True,
        "year": 2010,
    }
    url = reverse("movie:movie-list")
    response = client_api.post(url, content_data, format="json")
    assert response.status_code == 201


@pytest.mark.django_db()
def test__update_movie(client_api):
    older = MovieFactory(year=1980)
    content_data = {
        "year": 2010,
    }
    url = reverse("movie:movie-detail", args=[older.id])
    response = client_api.patch(url, content_data, format="json")
    assert response.status_code == 200


@pytest.mark.django_db()
def test__delete_movie(client_api):
    older = MovieFactory(year=1980)
    url = reverse("movie:movie-detail", args=[older.id])
    response = client_api.delete(url, format="json")
    assert response.status_code == 204

    response = client_api.get(url, format="json")
    assert response.status_code == 404
