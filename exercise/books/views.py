from datetime import datetime

from django.db.models import Avg, Count
from django_filters import rest_framework as filters
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer, MovieStatListSerializer


class MovieViewset(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("producer", "winner")


class MovieStatViewset(viewsets.ViewSet):
    def _generate_stat(self):
        query = (
            Movie.objects.values("producer")
            .annotate(cnt=Count("producer"))
            .filter(winner=True, cnt__gte=2)
        )

        min_list = []
        max_list = []
        for producer in query:
            producer_stat = self._process_producer(producer)
            min_list.append(
                {
                    "producer": producer["producer"],
                    "interval": producer_stat["min_interval"],
                    "previousWin": producer_stat["min_date"][0],
                    "followingWin": producer_stat["min_date"][1],
                }
            )
            max_list.append(
                {
                    "producer": producer["producer"],
                    "interval": producer_stat["max_interval"],
                    "previousWin": producer_stat["max_date"][0],
                    "followingWin": producer_stat["max_date"][1],
                }
            )
        return min_list, max_list

    def _order_producer_list(self, list_process, asc_direction=True):
        pass

    def _process_producer(self, producer):

        movie_start = Movie.objects.filter(producer=producer["producer"]).order_by(
            "year"
        )
        movie_next = None

        interval_winners = []
        interval_winners_date = []
        movie_reference_date = None

        for movie in movie_start:
            if movie_reference_date is None:
                movie_reference_date = movie.year
            else:
                interval_winners.append(movie.year - movie_reference_date)
                interval_winners_date.append((movie_reference_date, movie.year))
                movie_reference_date = movie.year

        min_interval = min(interval_winners)
        max_interval = max(interval_winners)
        min_interval_index = interval_winners.index(min_interval)
        max_interval_index = interval_winners.index(max_interval)

        return {
            "min_interval": min_interval,
            "max_interval": max_interval,
            "min_date": interval_winners_date[min_interval_index],
            "max_date": interval_winners_date[max_interval_index],
        }

    def list(self, request):
        min_list, max_list = self._generate_stat()
        to_serialize_data = {"min": min_list, "max": max_list}

        serializer = MovieStatListSerializer(to_serialize_data)
        return Response(serializer.data)
