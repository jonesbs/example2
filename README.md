# Instructions #

To correct installation of the API you need to already installed the pip and python 3
To local installation execute the follow command:

$ make prepare

To import CSV file you need add a file with the name "movielist.csv" at same folder together with this README file:
The CSV file need to be separated by ";" character.

$ make import

To start a local instance of the API, execute the follow command:

$ make local-run

To execute a tests:

$ make test

Endpoint to access:

GET http://localhost:8000/movie-stats/

The next endpoint accept methods: GET, POST, PUT, PATCH, DELETE and accept query_param filters: producer, winner
All methods http://localhost:8000/movie/

Do not forget add slash on final path to not return 404
No endpoints has access control or any kind of authentication process
