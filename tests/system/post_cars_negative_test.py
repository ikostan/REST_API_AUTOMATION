#!/path/to/interpreter

"""
Flask App REST API testing: POST
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import requests
from tests.system.base_test import BaseTestCase
from api.cars_app import USER_LIST


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API')
@allure.suite("System Tests")
@allure.sub_suite("Negative Tests")
@allure.feature("POST")
@allure.story('Cars')
class PostCarsPositiveTestCase(BaseTestCase):
    """
    Simple Flask App Negative Test: POST call
    """

    def setUp(self) -> None:
        """
        Test data preparation
        :return:
        """

        with allure.step("Prepare test data"):

            self.cars_url = '/cars'

            self.message = ''

            self.new_car = {'name': 'Figo',
                            'brand': 'Ford',
                            'price_range': '2-3 lacs',
                            'car_type': 'hatchback'}

    def test_post_car_wrong_admin_credentials(self):
        """
        Add new car using wrong admin user credentials.
        :return:
        """

        allure.dynamic.title("Add new car using wrong "
                             "admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[0]['name']
            password = USER_LIST[1]['password']
            self.assertEqual("admin",
                             USER_LIST[0]['perm'])

        with allure.step("Send POST request"):
            response = requests.post(self.URL +
                                     self.cars_url +
                                     '/add',
                                     json=self.new_car,
                                     auth=(username,
                                           password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_post_car_wrong_non_admin_credentials(self):
        """
        Add new car using wrong non admin user credentials.
        :return:
        """

        allure.dynamic.title("Add new car using wrong "
                             "non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[1]['name']
            password = USER_LIST[3]['password']
            self.assertEqual("non_admin",
                             USER_LIST[1]['perm'])

        with allure.step("Send POST request"):
            response = requests.post(self.URL +
                                     self.cars_url +
                                     '/add',
                                     json=self.new_car,
                                     auth=(username,
                                           password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])
