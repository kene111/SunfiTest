# SunfiTest


### Repo Structure:
ring: This is the django project (root directory) containing the django files.
lor: This is the django application.


### Implementation Stack:
1) Django REST Framework
2) Postgres (production db)
3) SQLite (development db)

### Choice for framework:
1) Familarity with django REST framework.
2) Django is more robust, compared to flask that is light weight framework.

### Test Cases:
1) Basic test cases were writting in order to test the API end points. This can be found using this path ->  rings/lor/tests.py

### Local Endpoint:

http://127.0.0.1:8000/characters/ - This endpoint is used to obtain the characters. (GET)
http://127.0.0.1:8000/characters/<str:id>/quotes/ -  This endpoint is used to obtain the quotes that belong to a character id. (GET)
http://127.0.0.1:8000/register/ - This endpoint is used to signup. (POST)
http://127.0.0.1:8000/login/ -  This endpoint is used for login. (POST)
http://127.0.0.1:8000/characters/<str:id>/favorites/ - This endpoint is used by authenticated users to favorite a specific character. (POST)
http://127.0.0.1:8000/characters/<str:char_id>/quotes/<str:quo_id>/favorites/ -  This endpoint is used by authenticated users to favorite a specific quote and character. (POST)
http://127.0.0.1:8000/favorites/ - This endpoint is used to get all entities liked by the authenticated user. (GET)

###### Challenges:
1) Deployment: 



