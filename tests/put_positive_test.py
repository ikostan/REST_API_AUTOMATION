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
@allure.feature("PUT")
@allure.story('Cars')
class PutCarsPositiveTestCase(BaseTestCase):
    """
    Simple Flask App Positive Test: PUT call > cars
    """

    def setUp(self) -> None:

        self.put_url = '/update/Vento'

        self.updated1 = {'name': 'Vento', 'brand': 'Ford',
                        'price_range': '2-3 lacs', 'car_type': 'sedan'}

        self.updated2 = {'name': 'Vento', 'brand': 'Ford',
                         'price_range': '3-5 lacs', 'car_type': 'convertible'}

    def test_put_update_car_admin(self):
        """
        Update car properties using admin user credentials.
        :return:
        """

        allure.dynamic.title("Get list of cars using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[0]['password']
            self.assertEqual("admin",
                             cars_app.user_list[0]['perm'])

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

        allure.dynamic.title("Get list of cars using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send PUT request"):
            response = requests.put(self.URL, auth=(username,
                                                    password))

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
