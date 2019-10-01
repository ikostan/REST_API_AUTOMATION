#!/path/to/interpreter

"""
Flask App REST API testing
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

            self.CARS_HATCHBACK = [{"name": "Swift",
                                    "brand": "Maruti",
                                    "price_range": "3-5 lacs",
                                    "car_type": "hatchback"},
                                   {"name": "Creta",
                                    "brand": "Hyundai",
                                    "price_range": "8-14 lacs",
                                    "car_type": "hatchback"}]

            self.CARS_SEDAN = [{"name": "City",
                                "brand": "Honda",
                                "price_range": "3-6 lacs",
                                "car_type": "sedan"},
                               {"name": "Vento",
                                "brand": "Volkswagen",
                                "price_range": "7-10 lacs",
                                "car_type": "sedan"}]

            self.CARS_LIST = cars_app.cars_list

    def test_get_list_of_cars_admin(self):
        """
        Get full list of cars using admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[0]['password']
            self.assertEqual("admin",
                             cars_app.user_list[0]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL, auth=(username,
                                                    password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertListEqual(self.CARS_LIST,
                                 response.json()['cars_list'])

    def test_get_list_of_cars_non_admin(self):
        """
        Get full list of cars using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL, auth=(username,
                                                    password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertListEqual(self.CARS_LIST,
                                 response.json()['cars_list'])

    def test_get_list_of_cars_non_admin_sedan(self):
        """
        Get full list of cars of type = 'sedan'
        using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars of type = 'sedan' using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL + '/filter/sedan',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify retrieved cars list"):
            self.assertListEqual(self.CARS_SEDAN,
                                 response.json()['cars'])

    def test_get_list_of_cars_admin_hatchback(self):
        """
        Get full list of cars from type = 'hatchback'
        using admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars of type = 'hatchback' using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[0]['password']
            self.assertEqual("admin",
                             cars_app.user_list[0]['perm'])

        with allure.step("Send GET request"):
            response = requests.get(self.URL + '/filter/hatchback',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify retrieved cars list"):
            self.assertListEqual(self.CARS_HATCHBACK,
                                 response.json()['cars'])

    def test_get_car_by_name_non_admin_swift(self):
        """
        Get car data by name = 'swift'
        using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Get car data by name using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Prepare expected results"):
            car = {"brand": "Maruti",
                   "car_type": "hatchback",
                   "name": "Swift",
                   "price_range": "3-5 lacs"}

        with allure.step("Send GET request"):
            response = requests.get(self.URL + '/Swift',
                                    auth=(username, password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved car data"):
            self.assertDictEqual(car,
                                 response.json()['car'])
