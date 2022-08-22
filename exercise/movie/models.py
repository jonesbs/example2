from django.db import models


class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    title = models.CharField(max_length=255, null=False)
    studio = models.CharField(max_length=255, null=False)
    producer = models.CharField(max_length=255, null=False)
    winner = models.BooleanField()
