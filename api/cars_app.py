#!/path/to/interpreter

"""
cars api is a sample web application developed by Qxf2 Services
to help testers learn API automation.

This REST application written in Python was built solely
to help QA learn to write API automation.

The application has endpoints for you to practice automating
GET, POST, PUT and DELETE methods.

It includes endpoints that use URL parameters, jSON payloads,
returns different response codes, etc.

We have also included permissions and authentication too
to help you write role based API tests.

IMPORTANT DISCLAIMER: The code here does not reflect
Qxf2's coding standards and practices.
"""

import os
import flask
import logging
from random import SystemRandom
from .data import TestData
from .internal_methods import requires_auth, requires_perm
from flask import Flask, request, jsonify, abort, render_template


app = Flask(__name__)

"""
Write logs for app file handler of logging module.
It is not creating log directory if dir does not exist.
"""
if not os.path.exists('log'):
    os.makedirs('log')
FILE_HANDLER = logging.FileHandler('log/app.log')
app.logger.addHandler(FILE_HANDLER)
app.logger.setLevel(logging.INFO)


@app.route("/", methods=["GET"])
def index_page():
    """
    This will help test GET without url params
    :return: rendered 'index.html' template
    """
    return render_template('index.html')


@app.route("/cars", methods=["GET"])
@requires_auth
def get_cars():
    """
    This will help test GET without url params
    :return: returns a list of cars
    :Example:

    response = requests.get(url='http://127.0.0.1:5000/cars',
    auth=(username,password))
    """
    return flask.jsonify({"cars_list": TestData.CARS_LIST, 'successful': True})


@app.route("/cars/<name>", methods=["GET"])
@requires_auth
def get_car_details(name):
    """
    This will help test GET with url params
    :param name: car name
    :return: car by name
    :Example:

    response = requests.get(url='http://127.0.0.1:5000/cars/Swift',
    auth=(username,password))
    """
    car = [car for car in TestData.CARS_LIST if car['name'] == name]
    if len(car) == 0:
        resp = jsonify({'message': 'No car found', 'successful': False}), 200
    else:
        resp = jsonify({'car': car[0], 'successful': True}), 200

    return resp


@app.route("/cars/find", methods=["GET"])
@requires_auth
def get_car():
    """
    This will help test GET with url params
    :return:
    """
    car_name = request.args.get('car_name')
    brand = request.args.get('brand')
    if car_name != "" and car_name is not None \
            and brand != "" and brand is not None:
        car = [car for car in TestData.CARS_LIST if car['name'] == car_name]
        if len(car) == 0:
            resp = jsonify({'message': 'No car found',
                            'successful': False}), 200
        else:
            resp = jsonify({'car': car[0], 'successful': True}), 200
    else:
        resp = jsonify(
            {'message': 'Not enough url_params', 'successful': False})

    return resp


@app.route("/cars/add", methods=["POST"])
@requires_auth
def add_car():
    """
    This will help test POST without url params.
    Add new cars.
    :return:
    :Example:

    response = requests.post(url='http://127.0.0.1:5000/cars/add',
    json={'name':'figo','brand':'Ford','price_range':'2-3lacs','car_type':'hatchback'},
    auth=(username,password))
    """
    if not request.json or 'name' not in request.json:
        resp = jsonify({'message': 'Not a json', 'successful': False, }), 400
    car = {
        'name': request.json['name'],
        'brand': request.json['brand'],
        'price_range': request.json['price_range'],
        'car_type': request.json['car_type']
    }
    TestData.CARS_LIST.append(car)
    resp = jsonify({'car': car, 'successful': True}), 200

    return resp


@app.route("/cars/update/<name>", methods=["PUT"])
@requires_auth
def update_car(name):
    """
    This will help test PUT
    Add new cars.
    :param name:
    :return:
    :Example:

    response = requests.post(url='http://127.0.0.1:5000/cars/add',
    json={'name':'figo','brand':'Ford','price_range':'2-3lacs','car_type':'hatchback'},
    auth=(username,password))
    """
    resp = {}
    car = [car for car in TestData.CARS_LIST if car['name'] == name]
    if len(car) != 0:
        if not request.json or 'name' not in request.json:
            resp['message'], resp['successful'] = 'Not a json'
            status_code = 404
        else:
            car[0]['name'] = request.json['name']
            car[0]['brand'] = request.json['brand']
            car[0]['price_range'] = request.json['price_range']
            car[0]['car_type'] = request.json['car_type']
            resp['car'], resp['successful'] = car[0], True
            status_code = 200

    else:
        resp['message'], resp['successful'] = 'No car found', False
        status_code = 404

    return jsonify({'response': resp}), status_code


@app.route("/cars/remove/<name>", methods=["DELETE"])
@requires_auth
def remove_car(name):
    """
    This will help test DELETE
    :param name:
    :return:
    :Example:

    response = requests.delete(
    url='http://127.0.0.1:5000/register/cars/remove/City',
    auth=(username,password))
    """
    car = [car for car in TestData.CARS_LIST if car['name'] == name]
    if len(car) == 0:
        abort(404)
    TestData.CARS_LIST.remove(car[0])

    return jsonify({'car': car[0], 'successful': True}), 200


@app.route('/register/car', methods=['POST'])
@requires_auth
def register_car():
    """
    This will help test GET and POST with dynamic numbers in url
    :return:
    """
    car_name = request.args.get('car_name')
    brand = request.args.get('brand')
    if car_name != "" and car_name is not None \
            and brand != "" and brand is not None:
        car = [car for car in TestData.CARS_LIST if car['name'] == car_name]
    customer_details = {
        'customer_name': request.json['customer_name'],
        'city': request.json['city']
    }
    # create a random number that is cryptographically secure in python
    # Source: https://stackoverflow.com/questions/20936993/
    # how-can-i-create-a-random-number-that-is-cryptographically-secure-in-python
    cryptogen = SystemRandom()
    registered_car = {'car': car[0], 'customer_details': request.json,
                      'registration_token': cryptogen.randrange(0, 4),
                      'successful': True}
    TestData.registered_cars.append(registered_car)

    return jsonify({'registered_car': registered_car})


@app.route('/register/', methods=['GET'])
@requires_auth
def get_registered_cars():
    """
    This will help test GET without url_params
    :return:
    """
    return jsonify({'registered': TestData.registered_cars, 'successful': True})


@app.route('/register/car/delete/', methods=['DELETE'])
@requires_auth
def delete_registered_cars():
    """
    This will help test delete.
    Delete first entry in car registration list.
    :return:
    :Example:

    response = requests.delete(url='http://127.0.0.1:5000/register/car/delete',
    auth=(username,password))
    """
    del TestData.registered_cars[0]

    return jsonify({'successful': True}), 200


@app.route('/cars/filter/<car_type>', methods=['GET'])
@requires_auth
def filter_cars(car_type):
    """
    Get cars of the given car type
    :param car_type: hatchback, sedan, etc...
    :return: filtered list (by car type) of cars
    :Example:

    response = requests.get(
    url='http://127.0.0.1:5000/cars/filter/hatchback',
    auth=(username,password))
    """
    filtered_list = [car for car in TestData.CARS_LIST if car['car_type'] == car_type]

    return jsonify({'cars': filtered_list})


@app.route('/users', methods=["GET"])
@requires_auth
def get_user_list():
    """
    Return user list if the given authenticated user has admin permission
    :return: the list of users or 403 error
    :Example:

    response = requests.get(url='http://127.0.0.1:5000/users',
    auth=(username,password))
    """
    if requires_perm() is True:
        return jsonify({'user_list': TestData.USER_LIST, 'successful': True}), 200

    return jsonify({'message': 'You are not permitted to access this resource',
                    'successful': False}), 403


if __name__ == "__main__":

    # Top-level script environment.
    # A module can discover whether or not it is running in
    # the main scope by checking its own __name__, which allows
    # a common idiom for conditionally executing code in a module
    # when it is run as a script or with python -m but not when it is imported.

    app.run(debug=False)
