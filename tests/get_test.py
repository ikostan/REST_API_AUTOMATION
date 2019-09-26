#!/path/to/interpreter

"""
Flask REST API testing
"""

import unittest
import requests
import cars_app


class GetTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:
		cls.URL = 'http://127.0.0.1:5000/cars'
		cls.CARS_LIST = [{"name": "Swift", "brand": "Maruti",
		              "price_range": "3-5 lacs", "car_type": "hatchback"},
		             {"name": "Creta", "brand": "Hyundai",
		              "price_range": "8-14 lacs", "car_type": "hatchback"},
		             {"name": "City", "brand": "Honda",
		              "price_range": "3-6 lacs", "car_type": "sedan"},
		             {"name": "Vento", "brand": "Volkswagen",
		              "price_range": "7-10 lacs", "car_type": "sedan"}]

	def test_get_list_of_cars_admin(self):
		username = cars_app.user_list[0]['name']
		password = cars_app.user_list[0]['password']
		self.assertEqual("admin", cars_app.user_list[0]['perm'])

		response = requests.get(self.URL, auth=(username, password))
		self.assertEqual(200, response.status_code)
		self.assertListEqual(self.CARS_LIST, response.json()['cars_list'])

	def test_get_list_of_cars_non_admin(self):
		username = cars_app.user_list[0]['name']
		password = cars_app.user_list[0]['password']
		self.assertEqual("non_admin", cars_app.user_list[1]['perm'])

		response = requests.get(self.URL, auth=(username, password))
		self.assertEqual(200, response.status_code)
		self.assertListEqual(self.CARS_LIST, response.json()['cars_list'])


if __name__ == "__main__":
	unittest.main()
