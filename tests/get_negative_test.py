#!/path/to/interpreter

"""
Flask App REST API testing: GET
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import requests
import cars_app
from tests.base_test import BaseTestCase


@allure.epic('Simple Flask App')
@allure.parent_suite('Integration Tests')
@allure.suite("REST API")
@allure.sub_suite("Negative Tests")
@allure.feature("GET")
@allure.story('Get List of Cars')
class GetCarsNegativeTestCase(BaseTestCase):
    """
    Simple Flask App Negative Test: GET call > cars
    """

    def setUp(self) -> None:
        """
        Test data preparation
        :return:
        """

        with allure.step("Prepare test data"):
            self.cars_url = '/cars'

    def test_get_list_of_cars_admin_wrong_credentials(self):
        """
        Get full list of cars using wrong admin user credentials.
        Wrong password + Correct username.
        Correct password + Wrong username.
        :return:
        """

        allure.dynamic.title("Get list of cars using wrong"
                             " admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("admin",
                             cars_app.user_list[0]['perm'])

        with allure.step("Send GET request with wrong credentials"):
            response = requests.get(self.URL + self.cars_url,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_get_list_of_cars_empty_credentials(self):
        """
        Get full list of cars using empty username/password.
        Empty password + Empty username.
        :return:
        """

        allure.dynamic.title("Get list of cars empty username/password")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        username = ''
        password = ''

        with allure.step("Send GET request with empty username/password"):
            response = requests.get(self.URL + self.cars_url,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_get_list_of_cars_non_admin_wrong_credentials(self):
        """
        Get full list of cars using wrong non admin user credentials.
        Wrong password + Correct username.
        Correct password + Wrong username.
        :return:
        """

        allure.dynamic.title("Get list of cars using wrong"
                             " non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[3]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send GET request "):
            response = requests.get(self.URL + self.cars_url,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_get_list_of_cars_non_admin_sedan_wrong_credentials(self):
        """
        Get full list of cars of type = 'sedan'
        using wrong non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars of type = 'sedan' "
                             "using wrong non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[3]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send GET request with wrong credentials"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/filter/sedan',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_get_list_of_cars_sedan_empty_credentials(self):
        """
        Get full list of cars of type = 'sedan'
        using empty credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars of type = 'sedan' "
                             "using empty credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        username = ''
        password = ''

        with allure.step("Send GET request with wrong credentials"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/filter/sedan',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_get_list_of_cars_admin_hatchback_wrong_credentials(self):
        """
        Get full list of cars from type = 'hatchback'
        using wrong admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars of type = 'hatchback' "
                             "using wrong admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("admin",
                             cars_app.user_list[0]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/filter/hatchback',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_get_car_by_name_non_admin_swift_wrong_credentials(self):
        """
        Get car data by name = 'swift'
        using wrong non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get car data by name using "
                             "wrong non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[3]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/Swift',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_get_car_by_name_swift_empty_credentials(self):
        """
        Get car data by name = 'swift'
        using empty user credentials.
        :return:
        """

        allure.dynamic.title("Get car data by name using "
                             "empty user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        username = ''
        password = ''

        with allure.step("Send GET request"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/Swift',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])
