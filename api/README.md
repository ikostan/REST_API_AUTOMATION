# cars-api

A sample REST application to help testers learn to write API automation 

## What is REST
REST is acronym for REpresentational State Transfer. It is architectural style for distributed hypermedia systems and was first presented by Roy Fielding in 2000 in his famous [dissertation](https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm).

Like any other architectural style, REST also does have it’s own [6 guiding constraints](https://restfulapi.net/rest-architectural-constraints/) which must be satisfied if an interface needs to be referred as RESTful. These principles are listed below.

----
### RUN
-----
To run cars api on local machine:
```bash
python cars_app.py`
```

----
### API ENDPOINTS & EXAMPLES
----
import requests

GET:

1. /cars - Get the list of cars. Example: 
```python
   response = requests.get(url='http://127.0.0.1:5000/cars',auth=(*username,*password))
```

2. /users - Get the list of users. Example:
```python
response = requests.get(url='http://127.0.0.1:5000/users',auth=(username,password))
```

3. /cars/filter/<car_type> - Filter through the list of cars. Example: 
```python
response = requests.get(url='http://127.0.0.1:5000/cars/filter/hatchback',auth=(username,password))
```

4. /register - Get registered cars. Example:
```python
response = requests.get(url='http://127.0.0.1:5000/register',auth=(username,password))
```

5. /cars/< name > - Get cars by name. Example:
```python 
response = requests.get(url='http://127.0.0.1:5000/cars/Swift',auth=(username,password))
```

POST:
1. /cars/add - Add new cars 
   Example: response = requests.post(url='http://127.0.0.1:5000/cars/add',json={'name':'figo','brand':'Ford','price_range':'2-3lacs','car_type':'hatchback'},auth=(username,password))

2. /register/car - Register cars
   Example: response = requests.post(url='http://127.0.0.1:5000/register/car',params={'car_name':'figo','brand':'Ford'},json={'customer_name': 'Unai Emery','city': 'London'},auth=(username,password))

PUT:
1. /cars/update/< name >      - Update car properties 
   Example: response = requests.put(url='http://127.0.0.1:5000/cars/update/Vento',json={'name':Vento,'brand':'Ford','price_range':'2-3lacs','car_type':'sedan'},auth=(username,password))

DELETE:
1. /cars/remove/< name >      - Delete cars from cars_list 
   Example: response = requests.delete(url='http://127.0.0.1:5000/register/cars/remove/City',auth=(username,password))

2. /car/delete/     - Delete first entry in car registration list
   Example: response = requests.delete(url='http://127.0.0.1:5000/register/car/delete',auth=(username,password))

* Get the username & password from user_list in the cars_app.py file