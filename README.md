

Accesing 3rd party credy API
GET https://demo.credy.in/api/v1/maya/movies/

For this we have passed paswword and username from System Environment variable
 
with URL 
http://localhost:8000/credy

for pages pass page parameter
http://localhost:8000/credy?page=3
http://localhost:8000/credy?page=5


------------------------------
To Register USER  and get acces token(change password from admin panel to change raw password there and to use it) :-

POST http://localhost:8000/register/
input :-

{
    “username”: <desired username>,
    “password”: <desired password>
}

example :-
{
    "username":"pankaj",
    "password":"pankaj@123"
}

output :-

example :-
{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjo3LCJ1c2VybmFtZSI6InBhbmthaiIsImV4cCI6MTY2NjM1MTI2MiwiZW1haWwiOiIifQ.zf30V0piPod5BlSgjBojQr6q98cJ9U0zubgyjgRPToU"
}

http://localhost:8000/api/token/


input

{
    "username":"abvppp",
    "password":"rajromeo10"
}

output

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2NzY0ODI3MSwiaWF0IjoxNjY2MzUyMjcxLCJqdGkiOiI0ZjQ5OGIyMDhlMGY0NDY1YjZmYjYxYTQ3NTcyYWYzNyIsInVzZXJfaWQiOjEwfQ.JVZBa7YSvpoXkqo42sP7X00fihA4HQzpWsjttNNrC1c",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjY3NjQ4MjcxLCJpYXQiOjE2NjYzNTIyNzEsImp0aSI6IjUzNGY5ZDk2NzgzNjRmMDA4Njg1ZTM1MTI2ZjFjNjYxIiwidXNlcl9pZCI6MTB9.MXyMolNfvsCDFsMx2wP7onpCEe4gSykBIEpGAffsi6s"
}


Copy Above acces token And add everytime when we make any Request ( As Barear Token)

Get All movies from Database

Get http://localhost:8000/movies
Output:-

{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Dhoom3",
            "description": "jdjdjdjdj",
            "genres": "drama",
            "uuid": "dfadf0a6-f5c4-48fb-929a-5cd534873ee4"
        }
    ]
}

Get Movie By UUID

GET http://localhost:8000/movie/7a5fd364-b4d4-457d-8bb6-2e6475eb391c/

OUTPUT:-

{
    "title": "Dhoom3",
    "description": "jdjdjdjdj",
    "genres": "drama",
    "uuid": "dfadf0a6-f5c4-48fb-929a-5cd534873ee4"
}


GET COLLECTION 
http://localhost:8000/collection/

Output

[
    {
        "uuid": "0388d6c9-63e4-4170-8cf9-65a220822d20",
        "title": "Collection1",
        "description": "This is sample Collection1 .",
        "movies": [
            {
                "uuid": "dfadf0a6-f5c4-48fb-929a-5cd534873ee4"
            }
        ]
    },
    {
        "uuid": "513beb49-8eef-4127-9aee-6cbef8de5a3a",
        "title": "Collection2",
        "description": "This is Sample Collection 2",
        "movies": []
    }
]

GET COLLECTION BY UUID
http://localhost:8000/collection/0388d6c9-63e4-4170-8cf9-65a220822d20


OUTPUT :-
{
    "uuid": "513beb49-8eef-4127-9aee-6cbef8de5a3a",
    "title": "Collection2",
    "description": "This is Sample Collection 2",
    "movies": []
}

POST COLLECTION
POST http://localhost:8000/collection/

OUTPUT:-

{
    “title”: “<Title of the collection>”,
    “description”: “<Description of the collection>”,
    “movies”: [
        {
            “title”: <title of the movie>,
            “description”: <description of the movie>,
            “genres”: <generes>,
            “uuid”: <uuid>
        }, ...
    ]
}

UPDATE COLLECTION
PUT http://localhost:8000/collection/<collection_uuid>/

INPUT:-
{
    “title”: <Optional updated title>,
    “description”: <Optional updated description>,
    “movies”: <Optional movie list to be updated>,
}




DELETE COLLECTION
DELETE http://localhost:8000/collection/<collection_uuid>/


CREATED CUSTOM MIDDLEWARE :- RequestCounterMiddleware

TO COUNT REQUEST
http://localhost:8000/request-count

TO RESET COUNT:-
http://localhost:8000/request-count/reset/