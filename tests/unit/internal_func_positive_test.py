#!/path/to/interpreter

"""
Flask App REST API testing: Unit Tests
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import allure
import unittest
from api.cars_app import app, check_auth, authenticate_error


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API')
@allure.suite("Unit Tests")
@allure.sub_suite("Positive Tests")
@allure.feature("Internal Functions")
@allure.story('Flags and Args Validation')
class InternalFuncPositiveTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:

		with allure.step("Arrange test data"):
			cls.admin_user = {"name": "qxf2",
			                  "password": "qxf2",
			                  "perm": "admin"}

			cls.non_admin_user = {"name": "jack",
			                      "password": "qxf2",
			                      "perm": "non_admin"}

	def test_debug_mode(self):
		"""
		Whether debug mode is enabled.

		When using flask run to start the development server,
		an interactive debugger will be shown for unhandled exceptions,
		and the server will be reloaded when code changes.
		The debug attribute maps to this config key. This is enabled
		when ENV is 'development' and is overridden by the FLASK_DEBUG
		environment variable. It may not behave as expected if set in code.

		Do not enable debug mode when deploying in production.

		Default: True if ENV is 'development', or False otherwise.
		:return:
		"""

		allure.dynamic.title("API flags validation")
		allure.dynamic.severity(allure.severity_level.CRITICAL)

		with allure.step("Verify DEBUG flag"):
			self.assertFalse(app.config['DEBUG'])

	def test_check_auth_admin(self):

		with allure.step("Verify check_auth flag using admin user"):
			self.assertTrue(check_auth(username=self.admin_user["name"],
			                           password=self.admin_user["password"]))

	def test_check_auth_non_admin(self):

		with allure.step("Verify check_auth flag using non admin user"):
			self.assertTrue(check_auth(username=self.non_admin_user["name"],
			                           password=self.non_admin_user["password"]))

	def test_authenticate_error_flag_true(self):

		with app.app_context():

			with allure.step("Arrange authenticate_error response"):
				response = authenticate_error(auth_flag=True)

			with allure.step("Verify status code"):
				self.assertEqual(401,
				                 response.status_code)

			with allure.step("Verify header"):
				self.assertEqual('Basic realm="Example"',
				                 response.headers['WWW-Authenticate'])

	def test_authenticate_error_flag_false(self):

		with app.app_context():

			with allure.step("Arrange authenticate_error response"):
				response = authenticate_error(auth_flag=False)

			with allure.step("Verify status code"):
				self.assertEqual(401,
				                 response.status_code)

			with allure.step("Verify header"):
				self.assertEqual('Basic realm="Example"',
				                 response.headers['WWW-Authenticate'])
