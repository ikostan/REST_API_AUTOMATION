#!/path/to/interpreter

"""
Flask App REST API testing: GET
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import requests
from tests.system.base_test import BaseTestCase
from api.cars_app import CARS_LIST, USER_LIST


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API')
@allure.suite("System Tests")
@allure.sub_suite("Positive Tests")
@allure.feature("GET")
@allure.story('Cars')
class GetCarsPositiveTestCase(BaseTestCase):
    """
    Simple Flask App Positive Test: GET call > cars
    """

    def setUp(self) -> None:
        """
        Test data preparation
        :return:
        """

        with allure.step("Arrange expected results (cars list)"):

            self.cars_url = '/cars'

            self.CARS_HATCHBACK = [car for car in CARS_LIST
                                   if car["car_type"] == 'hatchback']

            self.CARS_SEDAN = [car for car in CARS_LIST
                               if car["car_type"] == 'sedan']

            self.CARS_LIST = CARS_LIST

    def test_get_list_of_cars_admin(self):
        """
        Get full list of cars using admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars "
                             "using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[0]['name']
            password = USER_LIST[0]['password']
            self.assertEqual("admin",
                             USER_LIST[0]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL + self.cars_url,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertTrue(all(True for car in self.CARS_LIST
                                if car in response.json()['cars_list']))

    def test_get_list_of_cars_non_admin(self):
        """
        Get full list of cars using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars "
                             "using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[1]['name']
            password = USER_LIST[1]['password']
            self.assertEqual("non_admin",
                             USER_LIST[1]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL + self.cars_url,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertTrue(all(True for car in self.CARS_LIST
                                if car in response.json()['cars_list']))

    def test_get_list_of_cars_non_admin_sedan(self):
        """
        Get full list of cars of type = 'sedan'
        using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars of type = 'sedan' "
                             "using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[1]['name']
            password = USER_LIST[1]['password']
            self.assertEqual("non_admin",
                             USER_LIST[1]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/filter/sedan',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify retrieved cars list of type sedan"):
            self.assertTrue(all(True for car in self.CARS_SEDAN
                                if car in response.json()['cars']))

    def test_get_list_of_cars_admin_hatchback(self):
        """
        Get full list of cars from type = 'hatchback'
        using admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars of type = 'hatchback' "
                             "using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[0]['name']
            password = USER_LIST[0]['password']
            self.assertEqual("admin",
                             USER_LIST[0]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/filter/hatchback',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify retrieved cars list of type hatchback"):
            self.assertTrue(all(True for car in self.CARS_HATCHBACK
                                if car in response.json()['cars']))

    def test_get_car_by_name_non_admin_swift(self):
        """
        Get car data by name = 'swift'
        using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get car data by name using "
                             "non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[1]['name']
            password = USER_LIST[1]['password']
            self.assertEqual("non_admin",
                             USER_LIST[1]['perm'])

        with allure.step("Prepare expected results"):
            car = {"brand": "Maruti",
                   "car_type": "hatchback",
                   "name": "Swift",
                   "price_range": "3-5 lacs"}

        with allure.step("Send GET request"):
            response = requests.get(self.URL +
                                    self.cars_url +
                                    '/Swift',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved car"):
            self.assertTrue(car == response.json()['car'])
