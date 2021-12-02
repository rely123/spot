![1](https://user-images.githubusercontent.com/19244197/144340438-c8b673d5-acd7-44a3-85a2-c97e86193808.png)

Solution to each item.

Each item makes use of the Song model and the serializer assigned to that model.

1.  To search for songs. Make it so that you find word matches and you don't have to exactly match the name of a song with a search word. 
    Using the get method in which a parameter (pk) is received via url, which in this case would be the word to search for. 
    With the pk I make an SQL query which is executed with the .raw () method with which we obtain the results of the query. 
    The results are stored in an object and the serializer is used to return the data and list it.

2.  List the Top 50. When analyzing the data of the songs I did not find any field in which the popularity is indicated or serves for a 
    filter and taking into account the name of the list which is "Top Songs" it is understood that they are already ordered by popularity. 
    Then using the get method in which I perform an SQL query and execute it with the .raw () method, the results are obtained. 
    To which I apply serializer to be able to return them.

3.  Delete song. The elimination of a song is carried out by taking as an identifier the, id of a song. 
    Using the delete method, it receives a parameter (pk) which is the, id of the song and this is sent via URL. 
    I use the try and except inside the try the query is made to obtain the object corresponding to that id and when it exists it is eliminated 
    and a success message is returned. Inside the except, if the object corresponding to that id does not exist, an error message is displayed.

4.  Add song. To add a new song I made use of the post method in which the received data I apply the serializer then I verify if that data is 
    valid then these are saved in the database using the .save () method and the added data is returned and a message of success. 
    If the data sent is incorrect, an error message is displayed.

5.  Group by gender. Using the get method which receives a parameter (pk) that is the name of the genre to filter and is sent via URL. 
    Using the pk make a SQL query and then execute it with the .raw () method. The results are stored in an object and later 
    I apply the serializer to it in order to return the result.

7.  Use SQLite database instead of JSON file. For this, create a model in Django which has the fields and data type of each one. 
    When executing the migrations, this table is generated. Then create a python file called populate.py in which I create a connection with the database, 
    open and load the json file and create an SQL query which inserts the songs with their respective fields one by one through a for loop. 
    And I end the connection with the database.

8.  Authentication for endpoints. For authentication I did it by token using the restframework.authtoken provided by the same framework, 
    it is enough to define the form of authentication we want in the settings.py file and add to each view a statement with which it is verified 
    if it is authenticated. I make use of an endpoint so that the token corresponding to a user can be obtained, which uses the POST method 
    and the username and password are sent when they are correct, this returns the token of said user when they are incorrect, it displays an error message.
    
How my code is structured.

First, the model is defined with each field and data type. Like it defines a serializer for said model that acts on all its fields.
A class was created using APIView for each requested endpoint in which each class carries its protection to only be executed when it has a token. 
Then the method that corresponds to each one is defined within which the necessary queries are made and the serializer is used if necessary and as a 
final part a return of the data to be displayed is made.

For each view a url is assigned with which the endpoint can be accessed.

Running solution:

Necessary programs.
-Install Python 3.1

-Install django: pip install Django == 3.2.9

-Install django rest framework: pip install djangorestframework

-Make migrations: python manage.py makemigrations

-Run migrations: python manage.py migrate

-Run the file populate.py: python populate.py

-Create a superuser and fill in the requested data: python manage.py createsuperuser

-Run server: python manage.py runserver

-To obtain the authentication token and be able to execute the endpoints using an application to perform API tests, execute the following endpoint with the POST method. http://127.0.0.1:8000/songs/api-token-auth/ sending the username and password keys with their respective values. Using the POST method. These being the data that were entered in step 5.

-Save necessary token to access any of the other endpoints.

-Endpoints to be able to access add each one to the end of the address http://127.0.0.1:8000/songs/

   search/<str:pk>/
   
  Search by song name. Send by URL the name of the song replacing <str: pk> with the word. With GET method.
 
   list/
   
  List the TOP 50 songs. With GET method

   delete/<int:pk>/
   
  Delete a song. Send by URL the id of the song replacing <int: pk> by the id of the song to delete. With DELETE method

   add/
   
  Add a song. With POST method
  
  Requested fields
  {
    "songId" :,
    "yam":,
    "releaseDate":,
    "kind" :,
    "url" :,
    "artistName" :,
    "artistId" :,
    "artistUrl" :,
    "artworkUrl100" :,
    "genres":
  }
 
   group/<str: pk>/
   
  Show songs by genre. Send by URL the name of the genre replacing <str: pk> with the desired genre. Using GET method
