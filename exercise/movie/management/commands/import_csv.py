import numpy as np
from movie.models import Movie
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("filename", nargs="+")

    def handle(self, *args, **options):
        filename = options["filename"][0]
        path = f"./{filename}"
        result = np.genfromtxt(path, delimiter=";", skip_header=1, dtype=str)
        for line in result:
            movie = Movie()
            movie.year = int(line[0])
            movie.title = line[1]
            movie.studio = line[2]
            movie.producer = line[3]
            movie.winner = line[4] == "yes"
            movie.save()

        self.stdout.write(self.style.SUCCESS("Successfully CSV imported "))
