#!/path/to/interpreter

"""
POST Call Integration Test
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import base64
import allure
import unittest
from flask import json
from api.cars_app import app


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API')
@allure.suite("Integration Tests")
@allure.sub_suite("Positive Tests")
@allure.feature("POST")
@allure.story('Car Registration')
class PostCarRegistrationCallTestCase(unittest.TestCase):
    """
    Testing a JSON API implemented in Flask.
    POST Call Integration Test.

    The POST method is used to request that the
    origin server accept the entity enclosed in the
    request as a new subordinate of the resource
    identified by the Request-URI in the Request-Line.
    It essentially means that POST request-URI
    should be of a collection URI.

    POST is NOT idempotent.
    So if you retry the request N times,
    you will end up having N resources with N
    different URIs created on server.

    Use POST when you want to add a child resource
    under resources collection.
    """

    def setUp(self) -> None:
        with allure.step("Prepare test data"):

            self.new_car = {"car_name": "Creta",
                            "brand": "Hyundai"}

            self.url = '{}?car_name={}&brand={}'.format('/register/car',
                                                        self.new_car['car_name'],
                                                        self.new_car['brand'])

            self.customer = {'customer_name': 'Unai Emery',
                             'city': 'London'}

            self.non_admin_user = {"name": "eric",
                                   "password": "testqxf2",
                                   "perm": "non_admin"}

            self.admin_user = {"name": "qxf2",
                               "password": "qxf2",
                               "perm": "admin"}

    def test_post_register_car_non_admin(self):
        """
        Test POST (register car) call
        using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Add car using "
                             "POST call and non "
                             "admin credentials")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step("Send POST request"):

            response = app.test_client().post(
                self.url,
                data=json.dumps(self.customer),
                content_type='application/json',
                # Testing Flask application
                # with basic authentication
                # Source: https://gist.github.com/jarus/1160696
                headers={
                    'Authorization': 'Basic ' +
                                     base64.b64encode(bytes(self.non_admin_user['name'] +
                                                            ":" +
                                                            self.non_admin_user['password'],
                                                            'ascii')).decode('ascii')
                }
            )

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

    def test_post_register_car_admin(self):
        """
        Test POST (register car) call
        using admin user credentials.
        :return:
        """

        allure.dynamic.title("Add car using "
                             "POST call and admin "
                             "credentials")
        allure.dynamic.severity(allure.severity_level.NORMAL)

        with allure.step("Send POST request"):

            response = app.test_client().post(
                self.url,
                data=json.dumps(self.customer),
                content_type='application/json',
                # Testing Flask application
                # with basic authentication
                # Source: https://gist.github.com/jarus/1160696
                headers={
                    'Authorization': 'Basic ' +
                                     base64.b64encode(bytes(self.admin_user['name'] +
                                                            ":" +
                                                            self.admin_user['password'],
                                                            'ascii')).decode('ascii')
                }
            )

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)
