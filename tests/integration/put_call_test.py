#!/path/to/interpreter

"""
PUT Call Integration Test
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import base64
import allure
import unittest
from flask import json
from api.cars_app import app


class PutCallTestCase(unittest.TestCase):
	"""
    Testing a JSON API implemented in Flask.
    PUT Call Integration Test.

	PUT method requests for the enclosed entity be stored under
	the supplied Request-URI. If the Request-URI refers to an
	already existing resource – an update operation will happen,
	otherwise create operation should happen if Request-URI is a
	valid resource URI (assuming client is allowed to determine
	resource identifier).

	Use PUT when you want to modify a singular resource
	which is already a part of resources collection.
	PUT replaces the resource in its entirety.
	"""

	def setUp(self) -> None:

		with allure.step("Prepare test data"):

			self.car_original = {"name": "Creta",
			                     "brand": "Hyundai",
			                     "price_range": "8-14 lacs",
			                     "car_type": "hatchback"}

			self.car_updated = {"name": "Creta",
			                    "brand": "Hyundai",
			                    "price_range": "6-9 lacs",
			                    "car_type": "hatchback"}

			self.non_admin_user = {"name": "eric",
			                       "password": "testqxf2",
			                       "perm": "non_admin"}

			self.admin_user = {"name": "qxf2",
			                   "password": "qxf2",
			                   "perm": "admin"}

	def tearDown(self) -> None:
		pass

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

	def test_put_cars_update_non_admin(self):
		"""
		Test PUT call using non admin user credentials.
		:return:
		"""

		allure.dynamic.title("Update car properties using "
		                     "PUT call and non admin credentials")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Send PUT request"):
			response = app.test_client().put(
				'{}{}'.format('/cars/update/',
				              self.car_original['name']),
				data=json.dumps(self.car_updated),
				content_type='application/json',

				# Testing Flask application
				# with basic authentication
				# Source: https://gist.github.com/jarus/1160696
				headers={
					'Authorization': 'Basic ' +
					                 base64.b64encode(bytes(self.non_admin_user['name'] +
					                                        ":" +
					                                        self.non_admin_user['password'],
					                                        'ascii')).decode('ascii')
				}
			)

		with allure.step("Verify status code"):
			self.assertEqual(200, response.status_code)

		with allure.step("Convert response into JSON data"):
			data = json.loads(response.get_data(as_text=True))
		# print("\nDATA:\n{}\n".format(data))  # Debug only

		with allure.step("Verify 'successful' flag"):
			self.assertTrue(data['response']['successful'])

		with allure.step("Verify updated car data"):
			self.assertDictEqual(self.car_updated,
			                     data['response']['car'])

	def test_put_cars_update_admin(self):
		"""
		Test PUT call using admin user credentials.
		:return:
		"""

		allure.dynamic.title("Update car properties using "
		                     "PUT call and admin credentials")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Send PUT request"):
			response = app.test_client().put(
				'{}{}'.format('/cars/update/',
				              self.car_original['name']),
				data=json.dumps(self.car_updated),
				content_type='application/json',

				# Testing Flask application
				# with basic authentication
				# Source: https://gist.github.com/jarus/1160696
				headers={
					'Authorization': 'Basic ' +
					                 base64.b64encode(bytes(self.admin_user['name'] +
					                                        ":" +
					                                        self.admin_user['password'],
					                                        'ascii')).decode('ascii')
				}
			)

		with allure.step("Verify status code"):
			self.assertEqual(200, response.status_code)

		with allure.step("Convert response into JSON data"):
			data = json.loads(response.get_data(as_text=True))
		# print("\nDATA:\n{}\n".format(data))  # Debug only

		with allure.step("Verify 'successful' flag"):
			self.assertTrue(data['response']['successful'])

		with allure.step("Verify updated car data"):
			self.assertDictEqual(self.car_updated,
			                     data['response']['car'])
