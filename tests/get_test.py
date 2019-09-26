#!/path/to/interpreter

"""
Flask REST API testing
"""

import unittest
import requests
import cars_app


@allure.epic('ParaBank Web App')
@allure.parent_suite('End To End')
@allure.suite("User Login/Logout")
@allure.sub_suite("Positive Tests")
@allure.feature("Admin Page")
@allure.story('Login/Logout Functionality')
class GetCarsTestCase(unittest.TestCase):

	@classmethod
	def setUpClass(cls) -> None:

		cls.URL = 'http://127.0.0.1:5000/cars'

		cls.CARS_HATCHBACK = [{"name": "Swift",
		                       "brand": "Maruti",
		                       "price_range": "3-5 lacs",
		                       "car_type": "hatchback"},
		                      {"name": "Creta",
		                       "brand": "Hyundai",
		                       "price_range": "8-14 lacs",
		                       "car_type": "hatchback"}]

		cls.CARS_SEDAN = [{"name": "City",
		                   "brand": "Honda",
		                   "price_range": "3-6 lacs",
		                   "car_type": "sedan"},
		                  {"name": "Vento",
		                   "brand": "Volkswagen",
		                   "price_range": "7-10 lacs",
		                   "car_type": "sedan"}]

		cls.CARS_LIST = cls.CARS_HATCHBACK + cls.CARS_SEDAN

	def test_get_list_of_cars_admin(self):
		username = cars_app.user_list[0]['name']
		password = cars_app.user_list[0]['password']
		self.assertEqual("admin",
		                 cars_app.user_list[0]['perm'])

		response = requests.get(self.URL, auth=(username,
		                                        password))
		self.assertEqual(200,
		                 response.status_code)

		self.assertTrue(response.json()['successful'])

		self.assertListEqual(self.CARS_LIST,
		                     response.json()['cars_list'])

	def test_get_list_of_cars_non_admin(self):
		username = cars_app.user_list[1]['name']
		password = cars_app.user_list[1]['password']
		self.assertEqual("non_admin",
		                 cars_app.user_list[1]['perm'])

		response = requests.get(self.URL, auth=(username,
		                                        password))
		self.assertEqual(200,
		                 response.status_code)

		self.assertTrue(response.json()['successful'])

		self.assertListEqual(self.CARS_LIST,
		                     response.json()['cars_list'])

	def test_get_list_of_cars_non_admin_sedan(self):
		username = cars_app.user_list[1]['name']
		password = cars_app.user_list[1]['password']
		self.assertEqual("non_admin",
		                 cars_app.user_list[1]['perm'])

		response = requests.get(self.URL + '/filter/sedan',
		                        auth=(username, password))

		self.assertEqual(200,
		                 response.status_code)

		self.assertListEqual(self.CARS_SEDAN,
		                     response.json()['cars'])

	def test_get_list_of_cars_admin_hatchback(self):
		username = cars_app.user_list[0]['name']
		password = cars_app.user_list[0]['password']
		self.assertEqual("admin",
		                 cars_app.user_list[0]['perm'])

		response = requests.get(self.URL + '/filter/hatchback',
		                        auth=(username, password))

		self.assertListEqual(self.CARS_HATCHBACK,
		                     response.json()['cars'])

	def test_get_car_by_name_non_admin_swift(self):
		username = cars_app.user_list[1]['name']
		password = cars_app.user_list[1]['password']
		self.assertEqual("non_admin",
		                 cars_app.user_list[1]['perm'])

		car = {"brand": "Maruti",
		       "car_type": "hatchback",
		       "name": "Swift",
		       "price_range": "3-5 lacs"}

		response = requests.get(self.URL + '/Swift',
		                        auth=(username, password))

		self.assertEqual(200,
		                 response.status_code)

		self.assertTrue(response.json()['successful'])

		self.assertDictEqual(car,
		                     response.json()['car'])
