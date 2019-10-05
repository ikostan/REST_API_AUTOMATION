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
@allure.sub_suite("Positive Tests")
@allure.feature("POST")
@allure.story('Car Registration')
class PostCarRegistrationPositiveTestCase(BaseTestCase):
    """
    Simple Flask App Positive Test: POST call
    """

    def setUp(self) -> None:
        """
        Test data preparation
        :return:
        """

        with allure.step("Prepare test data"):
            self.register_url = '/register/car'

            self.customer = {'customer_name': 'Unai Emery',
                             'city': 'London'}

            self.new_car = {"car_name": "Creta",
                            "brand": "Hyundai"}

    def tearDown(self) -> None:
        """
        Post test procedure
        :return:
        """

        with allure.step("Remove new added car from the list"):
            pass

    def test_register_car_admin(self):
        """
        Register car using admin user credentials.
        :return:
        """

        allure.dynamic.title("Register car "
                             "using admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[0]['name']
            password = USER_LIST[0]['password']
            self.assertEqual("admin",
                             USER_LIST[0]['perm'])

        with allure.step("Send POST request"):
            response = requests.post(url=self.URL +
                                     self.register_url,
                                     params=self.new_car,
                                     json=self.customer,
                                     auth=(username,
                                           password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['registered_car']['successful'])

        with allure.step("Verify retrieved car details"):
            self.assertDictEqual({
                "name": "Creta",
                "brand": "Hyundai",
                "price_range": "8-14 lacs",
                "car_type": "hatchback"
            }, response.json()['registered_car']['car'])

        with allure.step("Verify retrieved customer details"):
            self.assertDictEqual(self.customer,
                                 response.json()['registered_car']['customer_details'])

    def test_register_car_non_admin(self):
        """
        Register car using non admin user credentials.
        :return:
        """

        allure.dynamic.title("Register car "
                             "using non admin user credentials")
        allure.dynamic.severity(allure.severity_level.BLOCKER)

        with allure.step("Verify user permissions"):
            username = USER_LIST[1]['name']
            password = USER_LIST[1]['password']
            self.assertEqual("non_admin",
                             USER_LIST[1]['perm'])

        with allure.step("Send POST request"):
            response = requests.post(url=self.URL +
                                     self.register_url,
                                     params=self.new_car,
                                     json=self.customer,
                                     auth=(username,
                                           password))

        with allure.step("Verify status code"):
            self.assertEqual(200,
                             response.status_code)

        with allure.step("Verify 'successful' flag"):
            self.assertTrue(response.json()['registered_car']['successful'])

        with allure.step("Verify retrieved car details"):
            self.assertDictEqual({
                "name": "Creta",
                "brand": "Hyundai",
                "price_range": "8-14 lacs",
                "car_type": "hatchback"
            }, response.json()['registered_car']['car'])

        with allure.step("Verify retrieved customer details"):
            self.assertDictEqual(self.customer,
                                 response.json()['registered_car']['customer_details'])
