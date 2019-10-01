#!/path/to/interpreter

"""
Flask App REST API testing: PUT
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
@allure.feature("PUT")
@allure.story('Update Car')
class PutCarNegativeTestCase(BaseTestCase):
    """
    Simple Flask App Negative Test: PUT call > cars
    """

    def setUp(self) -> None:

        self.put_url = '/cars/update/Vento'

        self.original = {"name": "Vento", "brand": "Volkswagen",
                         "price_range": "7-10 lacs", "car_type": "sedan"}

        self.updated1 = {'name': 'Vento', 'brand': 'Ford',
                         'price_range': '2-3 lacs', 'car_type': 'sedan'}

        self.updated2 = {'name': 'Vento', 'brand': 'Ford',
                         'price_range': '3-5 lacs', 'car_type': 'convertible'}

    def test_put_update_car_admin_wrong_credentials(self):
        """
        Update car properties using wrong admin user credentials.
        :return:
        """

        allure.dynamic.title("Update car using wrong admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("admin",
                             cars_app.user_list[0]['perm'])

        with allure.step("Send PUT request"):
            response = requests.put(self.URL + self.put_url,
                                    json=self.updated1,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])

    def test_put_update_car_non_admin_wrong_credentials(self):
        """
        Update car properties using wrong non admin user credentials.
        :return:
        """

        allure.dynamic.title("Update car using wrong non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[3]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send PUT request"):
            response = requests.put(self.URL + self.put_url,
                                    json=self.updated2,
                                    auth=(username,
                                          password))

        with allure.step("Verify status code"):
            self.assertEqual(401,
                             response.status_code)

        with allure.step("Verify error message"):
            self.assertEqual("Authenticate with proper credentials",
                             response.json()["message"])
