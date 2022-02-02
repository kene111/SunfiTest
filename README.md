# SunfiTest


### Repo Structure:
1) ring: This is the django project (root directory) containing the django files.
2) lor: This is the django application.


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

1) http://127.0.0.1:8000/characters/ - This endpoint is used to obtain the characters. (GET)
2) http://127.0.0.1:8000/characters/<str:id>/quotes/ -  This endpoint is used to obtain the quotes that belong to a character id. (GET)
3) http://127.0.0.1:8000/register/ - This endpoint is used to signup. (POST)
4) http://127.0.0.1:8000/login/ -  This endpoint is used for login. (POST)
5) http://127.0.0.1:8000/characters/<str:id>/favorites/ - This endpoint is used by authenticated users to favorite a specific character. (POST)
6) http://127.0.0.1:8000/characters/<str:char_id>/quotes/<str:quo_id>/favorites/ -  This endpoint is used by authenticated users to favorite a specific quote and character.     (POST)
7) http://127.0.0.1:8000/favorites/ - This endpoint is used to get all entities liked by the authenticated user. (GET)
8) http://127.0.0.1:8000/logout/ - This endpoint is used logout.


### Running The Application:
1) clone the repo in a desired directory locally.
2) create and activate a virtual enviroment.
3) install the dependencies in the requirementnts.txt
4) run the django application


###### Challenges:
1) Deployment: Due to certain AWS issues the api service was not deployed. This problem is being rectified.





