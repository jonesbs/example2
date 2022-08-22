import factory
from movie.models import Movie


class MovieFactory(factory.django.DjangoModelFactory):

    producer = "Jerry Weintraub"
    title = "Cruising"
    studio = "Lorimar Productions, United Artists"
    winner = True

    class Meta:
        model = Movie
