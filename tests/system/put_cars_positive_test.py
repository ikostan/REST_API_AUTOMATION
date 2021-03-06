#!/path/to/interpreter

"""
Flask App REST API testing: PUT
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
@allure.sub_suite("Positive Tests")
@allure.feature("PUT")
@allure.story('Cars')
class PutCarPositiveTestCase(BaseTestCase):
    """
    Simple Flask App Positive Test: PUT call > cars
    """

    def setUp(self) -> None:

        self.put_url = '/cars/update/Vento'

        self.original = {"name": "Vento", "brand": "Volkswagen",
                         "price_range": "7-10 lacs", "car_type": "sedan"}

        self.updated1 = {'name': 'Vento', 'brand': 'Ford',
                         'price_range': '2-3 lacs', 'car_type': 'sedan'}

        self.updated2 = {'name': 'Vento', 'brand': 'Ford',
                         'price_range': '3-5 lacs', 'car_type': 'convertible'}

    def tearDown(self) -> None:

        username = USER_LIST[0]['name']
        password = USER_LIST[0]['password']

        with allure.step("Restore original cars list"):
            requests.put(self.URL + self.put_url,
                         json=self.original,
                         auth=(username,
                               password))

    def test_put_update_car_admin(self):
        """
        Update car properties using admin user credentials.
        :return:
        """

        allure.dynamic.title("Update car using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[0]['name']
            password = USER_LIST[0]['password']
            self.assertEqual("admin",
                             USER_LIST[0]['perm'])

        with allure.step("Send PUT request"):
            response = requests.put(self.URL + self.put_url,
                                    json=self.updated1,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()["response"]['successful'])

        with allure.step("Verify retrieved car data"):
            self.assertDictEqual(self.updated1,
                                 response.json()["response"]['car'])

    def test_put_update_car_non_admin(self):
        """
        Update car properties using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Update car using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[1]['name']
            password = USER_LIST[1]['password']
            self.assertEqual("non_admin",
                             USER_LIST[1]['perm'])

        with allure.step("Send PUT request"):
            response = requests.put(self.URL + self.put_url,
                                    json=self.updated2,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()["response"]['successful'])

        with allure.step("Verify retrieved car data"):
            self.assertDictEqual(self.updated2,
                                 response.json()["response"]['car'])
