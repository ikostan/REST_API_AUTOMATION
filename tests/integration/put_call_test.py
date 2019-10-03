#!/path/to/interpreter

"""
PUT Call Integration Test
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import base64
import unittest
from flask import json
from api.cars_app import app


class PutCallTestCase(unittest.TestCase):
	"""
	Testing a JSON API implemented in Flask.
	PUT Call Integration Test.
	"""

	def test_debug_mode(self):
		self.assertFalse(app.config['DEBUG'])

	def test_put_cars_update(self):
		car = {"name": "Creta",
		       "brand": "Hyundai",
		       "price_range": "8-14 lacs",
		       "car_type": "hatchback"}

		user = {"name": "eric",
		        "password": "testqxf2",
		        "perm": "non_admin"}

		response = app.test_client().put(
			'{}{}'.format('/cars/update/',
			              car['name']),
			data=json.dumps(car),
			content_type='application/json',

			# Testing Flask application
			# with basic authentication
			# Source: https://gist.github.com/jarus/1160696
			headers={
				'Authorization': 'Basic ' + base64.b64encode(bytes(user['name'] +
				                                                   ":" +
				                                                   user['password'],
				                                                   'ascii')).decode('ascii')
			}
		)

		self.assertEqual(200, response.status_code)

		data = json.loads(response.get_data(as_text=True))
		print("\nDATA:\n{}\n".format(data))  # Debug only

		self.assertTrue(data['response']['successful'])
