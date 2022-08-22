from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class MovieStatSerializer(serializers.Serializer):

    producer = serializers.CharField()
    interval = serializers.IntegerField()
    previousWin = serializers.IntegerField()
    followingWin = serializers.IntegerField()


class MovieStatListSerializer(serializers.Serializer):

    vars()["min"] = MovieStatSerializer(many=True)  # min is a reserved name
    vars()["max"] = MovieStatSerializer(many=True)  # max is a reserved name
