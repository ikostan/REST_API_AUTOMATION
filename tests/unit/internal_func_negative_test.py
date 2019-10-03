#!/path/to/interpreter

"""
Flask App REST API testing: Unit Tests
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from api.cars_app import check_auth


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API')
@allure.suite("Unit Tests")
@allure.sub_suite("Negative Tests")
@allure.feature("Internal Functions")
@allure.story('Flags and Args Validation')
class InternalFuncNegativeTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:

		with allure.step("Arrange test data"):
			cls.admin_user = {"name": "qxf2",
			                  "password": "123",
			                  "perm": "admin"}

			cls.non_admin_user = {"name": "jack",
			                      "password": "123",
			                      "perm": "non_admin"}

	def test_check_auth_wrong_admin(self):

		with allure.step("Verify check_auth flag using admin user"):
			self.assertFalse(check_auth(username=self.admin_user["name"],
			                            password=self.admin_user["password"]))

	def test_check_auth_wrong_non_admin(self):

		with allure.step("Verify check_auth flag using non admin user"):
			self.assertFalse(check_auth(username=self.non_admin_user["name"],
			                            password=self.non_admin_user["password"]))
