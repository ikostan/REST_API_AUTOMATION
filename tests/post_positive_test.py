#!/path/to/interpreter

"""
Flask App REST API testing: POST
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
@allure.feature("POST")
@allure.story('Add/Register New Cars')
class PostCarsPositiveTestCase(BaseTestCase):
    """
    Simple Flask App Positive Test: POST call
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

    def tearDown(self) -> None:
        """
        Post test procedure
        :return:
        """

        with allure.step("Remove new added car from the list"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[0]['password']

            requests.delete(url=self.URL +
                            self.cars_url +
                            '/remove/' +
                            self.new_car['name'],
                            auth=(username,
                                  password))

    def test_post_car_admin(self):
        """
        Add new car using admin user credentials.
        :return:
        """

        allure.dynamic.title("Add new car "
                             "using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[0]['name']
            password = cars_app.user_list[0]['password']
            self.assertEqual("admin",
                             cars_app.user_list[0]['perm'])

        with allure.step("Send POST request"):
            response = requests.post(self.URL +
                                     self.cars_url +
                                     '/add',
                                     json=self.new_car,
                                     auth=(username,
                                           password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertDictEqual(self.new_car,
                                 response.json()['car'])

    def test_post_car_non_admin(self):
        """
        Add new car using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Add new car "
                             "using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = cars_app.user_list[1]['name']
            password = cars_app.user_list[1]['password']
            self.assertEqual("non_admin",
                             cars_app.user_list[1]['perm'])

        with allure.step("Send POST request"):
            response = requests.post(self.URL +
                                     self.cars_url +
                                     '/add',
                                     json=self.new_car,
                                     auth=(username,
                                           password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['successful'])

        with allure.step("Verify retrieved cars list"):
            self.assertDictEqual(self.new_car,
                                 response.json()['car'])
