"""
cars api is a sample web application developed by
Qxf2 Services to help testers learn API automation.
This REST application written in Python was built
solely to help QA learn to write API automation.
The application has endpoints for you to practice
automating GET, POST, PUT and DELETE methods.
It includes endpoints that use URL parameters,
jSON payloads, returns different response codes, etc.
We have also included permissioning and authentication
too to help you write role based API tests.

IMPORTANT DISCLAIMER: The code here does not reflect
Qxf2's coding standards and practices.

Source: https://github.com/qxf2/cars-api
"""

import os
import logging
import random
import flask
from functools import wraps
from flask import Flask, request, jsonify, abort, render_template
from api.data.cars import Cars
from api.data.users import Users

app = Flask(__name__)
# write logs for app filehandler of logging  module
# is not creating log directory if dir does not exist
if not os.path.exists('log'):
    os.makedirs('log')
file_handler = logging.FileHandler('log/app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)

CARS_LIST = Cars().get_cars()

USER_LIST = Users().get_users()

REGISTERED_CARS = []


def check_auth(username, password):
    """
    check if the given is valid
    :param username:
    :param password:
    :return:
    """
    user = [user for user in USER_LIST if user['name']
            == username and user['password'] == password]
    if len(user) == 1:
        return True
    return False


def authenticate_error(auth_flag):
    """
    set auth message based on the
    authentication check result
    :param auth_flag:
    :return:
    """
    if auth_flag is True:
        message = {'message': "Authenticate with proper credentials"}
    else:
        message = {'message': "Require Basic Authentication"}
    resp = jsonify(message)
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
    return resp


def requires_auth(f):
    """
    verify given user authentication details
    :param f:
    :return:
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        auth_flag = True

        if not auth:
            auth_flag = False
            return authenticate_error(auth_flag)
        elif not check_auth(auth.username, auth.password):
            return authenticate_error(auth_flag)
        return f(*args, **kwargs)
    return decorated


def requires_perm():
    """
    check if the authenticated user has a admin permission
    :return:
    """
    auth = request.authorization
    perm_flag = False
    for user in USER_LIST:
        if user['name'] == auth.username and user['perm'] == 'admin':
            perm_flag = True
            return perm_flag
    return perm_flag


@app.route("/", methods=["GET"])
def index_page():
    """
    this will help test GET without url params
    :return:
    """
    return render_template('index.html')


@app.route("/cars", methods=["GET"])
@requires_auth
def get_cars():
    """
    this will help test GET without url params
    :return:
    """
    return flask.jsonify({"cars_list": CARS_LIST,
                          'successful': True})


@app.route("/cars/<name>", methods=["GET"])
@requires_auth
def get_car_details(name):
    """
    this will help test GET with url params
    :param name:
    :return:
    """
    car = [car for car in CARS_LIST if car['name'] == name]
    if len(car) == 0:
        resp = jsonify({'message': 'No car found',
                        'successful': False}), 200
    else:
        resp = jsonify({'car': car[0],
                        'successful': True}), 200
    return resp


@app.route("/cars/find", methods=["GET"])
@requires_auth
def get_car():
    """
    this will help test GET with url params
    :return:
    """
    car_name = request.args.get('car_name')
    brand = request.args.get('brand')
    if car_name != "" and \
            car_name is not None and \
            brand != "" and brand is not None:
        car = [car for car in CARS_LIST if car['name'] == car_name]
        if len(car) == 0:
            resp = jsonify({'message': 'No car found',
                            'successful': False}), 200
        else:
            resp = jsonify({'car': car[0], 'successful': True}), 200
    else:
        resp = jsonify(
            {'message': 'Not enough url_params',
             'successful': False})
    return resp


@app.route("/cars/add", methods=["POST"])
@requires_auth
def add_car():
    """
    this will help test POST without url params
    :return:
    """
    if not request.json or 'name' not in request.json:
        resp = jsonify({'message': 'Not a json',
                        'successful': False, }), 400
    car = {
        'name': request.json['name'],
        'brand': request.json['brand'],
        'price_range': request.json['price_range'],
        'car_type': request.json['car_type']
    }
    CARS_LIST.append(car)
    resp = jsonify({'car': car, 'successful': True}), 200
    return resp


@app.route("/cars/update/<name>", methods=["PUT"])
@requires_auth
def update_car(name):
    """
    this will help test PUT
    :param name:
    :return:
    """
    resp = {}
    car = [car for car in CARS_LIST if car['name'] == name]
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
    this will help test DELETE
    :param name:
    :return:
    """
    car = [car for car in CARS_LIST if car['name'] == name]
    if len(car) == 0:
        abort(404)
    CARS_LIST.remove(car[0])
    return jsonify({'car': car[0], 'successful': True}), 200


@app.route('/register/car', methods=['POST'])
@requires_auth
def register_car():
    """
    this will help test GET and POST with dynamic numbers in url
    :return:
    """
    car_name = request.args.get('car_name')
    brand = request.args.get('brand')
    if car_name != "" and car_name is not None and brand != "" and brand is not None:
        car = [car for car in CARS_LIST if car['name'] == car_name]
    customer_details = {
        'customer_name': request.json['customer_name'],
        'city': request.json['city']
    }
    registered_car = {'car': car[0], 'customer_details': request.json,
                      'registration_token': random.randrange(0, 4), 'successful': True}
    REGISTERED_CARS.append(registered_car)
    return jsonify({'registered_car': registered_car})


@app.route('/register/', methods=['GET'])
@requires_auth
def get_registered_cars():
    """
    this will help test GET without url_params
    :return:
    """
    return jsonify({'registered': REGISTERED_CARS,
                    'successful': True})


@app.route('/register/car/delete/', methods=['DELETE'])
@requires_auth
def delete_registered_cars():
    """
    this will help test delete
    :return:
    """
    del REGISTERED_CARS[0]
    return jsonify({'successful': True}), 200


@app.route('/cars/filter/<car_type>', methods=['GET'])
@requires_auth
def filter_cars(car_type):
    """
    get cars of the given car type
    :param car_type:
    :return:
    """
    filtered_list = [car for car in CARS_LIST if car['car_type'] == car_type]
    return jsonify({'cars': filtered_list})


@app.route('/users', methods=["GET"])
@requires_auth
def get_user_list():
    """
    return user list if the given
    authenticated user has admin permission
    :return:
    """
    if requires_perm() is True:
        return jsonify({'user_list': USER_LIST,
                        'successful': True}), 200
    return jsonify({'message': 'You are not '
                               'permitted to access this resource',
                    'successful': False}), 403


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
