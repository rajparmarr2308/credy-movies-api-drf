from itertools import count
from pydoc import resolve
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics, status
from movie.serializers import MovieSerializer, CollectionSerializer
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings

from django.conf import settings
from movie.models import Movie, Collection
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
import requests
from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
from movie_collection.settings import username
from movie_collection.settings import password
from movie import middleware
from movie.middleware import RequestCounterMiddleware


#for localhost:8000/movies
def AccessThirdPartyView(request):

    url="https://demo.credy.in/api/v1/maya/movies/"
    moviedata={}
    

    page=request.GET.get("page")
    if page==None:
        try:
            response = requests.get(url,auth = HTTPBasicAuth(username, password))
            moviedata = response.json()
   
        except ConnectionError as e:  
            print('connection error occurred')
    else:
        pagin_url=url+"?page="+str(page)
        
        try:
            response = response = requests.get(pagin_url,auth = HTTPBasicAuth(username, password))
            moviedata = response.json()
            
            
        except ConnectionError as e:  
            print('connection error occurred')
    

    return JsonResponse(moviedata)

class MovieViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MovieSerializer
    pagination_class=PageNumberPagination

class CollectionViewSet(viewsets.ModelViewSet):
    lookup_field = "uuid"
    queryset = Collection.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = CollectionSerializer
    pagination_class=PageNumberPagination

    # def list(self, request):
    #     serializer = self.get_serializer(self.queryset, many=True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self,request,*args,**kwargs):
        instance = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(instance)
        response = None
        
        if page is not None:
            serializer = self.get_serializer(page,many=True)
            response = self.get_paginated_response(serializer.data)
            response.data["license_info"] = OrderedDict(
                                [
                                    ("key", "value"),
                                ]
                            )
        else:
            serializer = self.get_serializer(instance,many=True)
            response_data = []
            response_data.extend(serializer.data)
            response_data.append({"license_info":"some value"})
            response = Response(response_data)
        
        return response

@api_view(['GET', 'POST'])
def ProcessRequestCount(request):
    if request.method == 'GET':
        
        count=middleware.count
        
        return JsonResponse({"requests":count})
       
 
    elif request.method == 'POST':
        middleware.count=0
        return JsonResponse({"message":"request count reset successfully"})
        
# class CustomLimitOffsetPagination(JsonApiLimitOffsetPagination):
    
#     def get_paginated_response(self, data):
#         return Response(
#             {
#                 "results": data,
#                 "meta": {
#                     "pagination": OrderedDict(
#                         [
#                             ("count", self.count),
#                             ("limit", self.limit),
#                             ("offset", self.offset),
#                         ]
#                     )
#                 },
#                 "links": OrderedDict(
#                     [
#                         ("first", self.get_first_link()),
#                         ("last", self.get_last_link()),
#                         ("next", self.get_next_link()),
#                         ("prev", self.get_previous_link()),
#                     ]
#                 ),
#               #Extra dictionary 
#               "favourite_genres":Collection.objects.values('uuid').annotate(movie_gernes_count=Count('movie')).order_by('-movie_gernes_count')[:5],

#             }
#         )


@api_view(['POST'])
@permission_classes([AllowAny, ])
def authenticate_user(request):
    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    data = request.data
    user = User.objects.create(username=data['username'])
    user.set_password(data['password'])
    
    if user:
        try:
            payload = jwt_payload_handler(user)
            token = jwt.encode(payload, settings.SECRET_KEY)
            return Response({'access_token': token }, status=status.HTTP_200_OK)
        except Exception as e:
            raise e
    else:
        res = {
            'error': 'can not authenticate with the given credentials or the account has been deactivated'}
        return Response(res, status=status.HTTP_403_FORBIDDEN)


# Get DATA From API and PUT IN DATABASE
# response = requests.get(url)
# data1=response.json()
# if "count" in data1:
#     l1=data1['results']
    
    
#     print(l1)
#     for i in l1:    
#         obj=Movie(title=i['title'],description=i['description'],genres=i['genres'],uuid=i['uuid'])
#         obj.save()
# else:
#     print("Key doesn't exist in JSON data Refresh page/HIT API Again")

# url2=data1["next"]


# while url2!="null":
#     response = requests.get(url2)
#     data2=response.json()
#     if "count" in data2:
#         l2=data2['results']
#         url2=data2["next"]

#         for i in l2:    
#             obj=Movie(title=i['title'],description=i['description'],genres=i['genres'],uuid=i['uuid'])
#             obj.save()
#     else:
#         print("Key doesn't exist in JSON data Refresh page/HIT API Again")