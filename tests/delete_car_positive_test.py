#!/path/to/interpreter

"""
Flask App REST API testing: DELETE
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import requests
from tests.base_test import BaseTestCase
from api.cars_app import CARS_LIST, USER_LIST


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API Integration Tests')
@allure.suite("Cars")
@allure.sub_suite("Positive Tests")
@allure.feature("DELETE")
@allure.story('DELETE Car')
class DeleteCarPositiveTestCase(BaseTestCase):
    """
    Simple Flask App Positive Test: DELETE call > cars
    """

    def setUp(self) -> None:
        """
        Test data preparation
        :return:
        """

        with allure.step("Arrange expected results (cars list)"):
            self.post_url = '/cars/add'
            self.delete_car_url = '/cars/remove/'
            self.cars = CARS_LIST
            self.car = {"name": "City",
                        "brand": "Honda",
                        "price_range": "3-6 lacs",
                        "car_type": "sedan"}

    def tearDown(self) -> None:

        username = USER_LIST[0]['name']
        password = USER_LIST[0]['password']

        with allure.step("Restore original cars list"):
            requests.post(url=self.URL + self.post_url,
                          json=self.car,
                          auth=(username,
                                password))

    def test_delete_car_admin(self):
        """
        Delete car using admin user credentials.
        :return:
        """

        allure.dynamic.title("Delete car "
                             "using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[0]['name']
            password = USER_LIST[0]['password']
            self.assertEqual("admin",
                             USER_LIST[0]['perm'])

        with allure.step("Send DELETE request"):
            response = requests.delete(url='{}{}{}'.format(self.URL,
                                                           self.delete_car_url,
                                                           self.car['name']),
                                       auth=(username,
                                             password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertDictEqual(self.car,
                                 response.json()['car'])

    def test_delete_car_non_admin(self):
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

        with allure.step("Send DELETE request"):
            response = requests.delete(url='{}{}{}'.format(self.URL,
                                                           self.delete_car_url,
                                                           self.car['name']),
                                       auth=(username,
                                             password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertDictEqual(self.car,
                                 response.json()['car'])
