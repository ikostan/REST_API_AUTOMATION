#!/path/to/interpreter

"""
PUT Call Integration Test
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import base64
import unittest

import allure
from flask import json
from api.cars_app import app


class PutCallTestCase(unittest.TestCase):
	"""
    Testing a JSON API implemented in Flask.
    PUT Call Integration Test.
    """

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

	def test_put_cars_update(self):
		"""
		PUT method requests for the enclosed entity be stored under
		the supplied Request-URI. If the Request-URI refers to an
		already existing resource – an update operation will happen,
		otherwise create operation should happen if Request-URI is a
		valid resource URI (assuming client is allowed to determine
		resource identifier).
		:return:
		"""
		allure.dynamic.title("Update car properties using PUT call")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Prepare test data"):
			car = {"name": "Creta",
			       "brand": "Hyundai",
			       "price_range": "8-14 lacs",
			       "car_type": "hatchback"}

			user = {"name": "eric",
			        "password": "testqxf2",
			        "perm": "non_admin"}

		with allure.step("Send PUT request"):
			response = app.test_client().put(
				'{}{}'.format('/cars/update/',
				              car['name']),
				data=json.dumps(car),
				content_type='application/json',

				# Testing Flask application
				# with basic authentication
				# Source: https://gist.github.com/jarus/1160696
				headers={
					'Authorization': 'Basic ' +
					                 base64.b64encode(bytes(user['name'] +
					                                        ":" +
					                                        user['password'],
					                                        'ascii')).decode('ascii')
				}
			)

		with allure.step("Verify status code"):
			self.assertEqual(200, response.status_code)

		with allure.step("Convert response into JSON data"):
			data = json.loads(response.get_data(as_text=True))
			print("\nDATA:\n{}\n".format(data))  # Debug only

		with allure.step("Verify 'successful' flag"):
			self.assertTrue(data['response']['successful'])
