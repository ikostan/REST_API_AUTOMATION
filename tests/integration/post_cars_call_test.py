#!/path/to/interpreter

"""
POST Call Integration Test
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import base64
import allure
import unittest
from flask import json
from api.cars_app import app, CARS_LIST


@allure.epic('Simple Flask App')
@allure.parent_suite('REST API')
@allure.suite("Integration Tests")
@allure.sub_suite("Positive Tests")
@allure.feature("POST")
@allure.story('Add New Car')
class PostCarsCallTestCase(unittest.TestCase):
	"""
    Testing a JSON API implemented in Flask.
    POST Call Integration Test.

	The POST method is used to request that the
	origin server accept the entity enclosed in the
	request as a new subordinate of the resource
	identified by the Request-URI in the Request-Line.
	It essentially means that POST request-URI
	should be of a collection URI.

	POST is NOT idempotent.
	So if you retry the request N times,
	you will end up having N resources with N
	different URIs created on server.

	Use POST when you want to add a child resource
	under resources collection.
	"""

	def setUp(self) -> None:
		with allure.step("Prepare test data"):

			self.new_car = {"name": "Punto",
			                "brand": "Fiat",
			                "price_range": "1-3 lacs",
			                "car_type": "hatchback"}

			self.non_admin_user = {"name": "eric",
			                       "password": "testqxf2",
			                       "perm": "non_admin"}

			self.admin_user = {"name": "qxf2",
			                   "password": "qxf2",
			                   "perm": "admin"}

	def test_post_car_non_admin(self):
		"""
		Test POST call using non admin user credentials.
		:return:
		"""

		allure.dynamic.title("Add car using "
		                     "POST call and non "
		                     "admin credentials")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Send PUT request"):
			response = app.test_client().post(
				'{}'.format('/cars/add'),
				data=json.dumps(self.new_car),
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
			self.assertTrue(data['successful'])

		with allure.step("Verify new car data"):
			self.assertDictEqual(self.new_car, data['car'])

	def test_post_car_admin(self):
		"""
		Test POST call using admin user credentials.
		:return:
		"""

		allure.dynamic.title("Add car using "
		                     "POST call and admin "
		                     "credentials")
		allure.dynamic.severity(allure.severity_level.NORMAL)

		with allure.step("Send PUT request"):
			response = app.test_client().post(
				'{}'.format('/cars/add'),
				data=json.dumps(self.new_car),
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
			self.assertTrue(data['successful'])

		with allure.step("Verify new car data"):
			self.assertDictEqual(self.new_car, data['car'])
