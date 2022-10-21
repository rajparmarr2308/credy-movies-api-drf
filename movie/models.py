from django.db import models
from uuid import uuid4
import uuid

"""This Model is for Movie Database"""
class Movie(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    genres = models.CharField(max_length=250)
    uuid = models.UUIDField(default=uuid4, editable=False, primary_key=True)

    def __str__(self):
        return self.title

"""This Model is for Collection Database"""
class Collection(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    movies = models.ManyToManyField(
        Movie,
        related_name="collections",
        through="MovieCollection",
        through_fields=("collection", "movie"),
    )

"""This Model is to map movies with collection  Database"""
class MovieCollection(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)



