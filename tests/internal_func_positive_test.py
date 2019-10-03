#!/path/to/interpreter

"""
Flask App REST API testing: GET
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from api.cars_app import app, check_auth, authenticate_error, requires_auth, requires_perm


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API Unit Tests')
@allure.suite("Internal Functions")
@allure.sub_suite("Positive Tests")
@allure.feature("Flags and Args")
@allure.story('Flags and Args Validation')
class InternalFuncPositiveTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.admin_user = {"name": "qxf2", "password": "qxf2", "perm": "admin"}
		cls.non_admin_user = {"name": "jack", "password": "qxf2", "perm": "non_admin"}

	def test_check_auth_admin(self):

		with allure.step("Verify check_auth flag using admin user"):
			self.assertTrue(check_auth(username=self.admin_user["name"],
			                           password=self.admin_user["password"]))

	def test_check_auth_non_admin(self):

		with allure.step("Verify check_auth flag using non admin user"):
			self.assertTrue(check_auth(username=self.non_admin_user["name"],
			                           password=self.non_admin_user["password"]))

	def test_authenticate_error(self):

		with app.app_context():

			with allure.step("Arrange authenticate_error response"):
				response = authenticate_error(auth_flag=True)

			with allure.step("Verify status code"):
				self.assertEqual(401,
				                 response.status_code)

			with allure.step("Verify header"):
				self.assertEqual('Basic realm="Example"',
				                 response.headers['WWW-Authenticate'])
