import uuid
from django.test import TestCase
import movie
from rest_framework.test import APITestCase
from uuid import uuid4
from movie.models import Movie, Collection,MovieCollection
from django.shortcuts import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

# Create your tests here.
class TestNoteApi(APITestCase):
    client = APIClient()
    def setUp(self):
        # create movie
        self.movie = Movie(title="The Space Between Us", description="des1",genres="Drama")
        self.movie.save()        
        id1=self.movie.uuid

        self.collection = Collection(title="Col1", description="desc collection")
        self.collection.save()
        id2=self.collection.uuid

        Collection.movies.through.objects.get_or_create(movie_id=id1,collection_id=id2)

        
        

    def test_movie_creation(self):
        self.assertEqual(Movie.objects.count(), 1)

     #for creating collections
    def test_adding_collections(self):
        self.assertEqual(Collection.objects.count(), 1)

    def test_movie_representation(self):
        self.assertEquals(self.movie.title, str(self.movie))


    def test_getting_movies(self):
        response = self.client.get('/movies/', format="json")
        self.assertEqual(len(response.data), 1)

    def test_getting_collections(self):
        response = self.client.get('/collection/', format="json")
        self.assertEqual(len(response.data), 1)

   

    def test_deleting_collections(self):
        response = self.client.get("/collection/0975453cba13456aa739ac1e2cc7295b/", format="json")
        # 401 means request is unauthorized  that's it
        self.assertEqual(204, response.status_code)

 
        