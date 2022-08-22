import re

import numpy as np
from django.core.management.base import BaseCommand
from movie.models import Movie


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument("filename", nargs="+")

    def split_producers(self, producer):
        response = re.split(r"(,| and |,and )", producer)
        response = [x for x in response if x not in [",", " and ", ",and "]]

        filter(lambda a: a.strip(), response)
        return response

    def handle(self, *args, **options):
        filename = options["filename"][0]
        path = f"./{filename}"
        result = np.genfromtxt(path, delimiter=";", skip_header=1, dtype=str)
        for line in result:
            for producer in self.split_producers(line[3]):
                movie = Movie()
                movie.year = int(line[0])
                movie.title = line[1]
                movie.studio = line[2]
                movie.producer = producer
                movie.winner = line[4] == "yes"
                movie.save()

        self.stdout.write(self.style.SUCCESS("Successfully CSV imported "))
