#!/path/to/interpreter

"""
Flask App REST API testing
"""

import unittest
import allure
import requests
import cars_app


@allure.epic('Simple Flask App')
@allure.parent_suite('Integration Tests')
@allure.suite("REST API")
@allure.sub_suite("Positive Tests")
@allure.feature("GET")
@allure.story('Cars')
class GetCarsTestCase(unittest.TestCase):
	"""
	Simple Flask App Test: GET call > cars
	"""

	@classmethod
	def setUpClass(cls) -> None:
		"""
		Test data preparation
		:return:
		"""

		with allure.step("Set test URL"):
			cls.URL = 'http://127.0.0.1:5000/cars'

		with allure.step("Arrange expected results (cars list)"):
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
		"""
		Get full list of cars using admin user credentials.
		:return:
		"""

		with allure.step("Verify user permissions"):
			username = cars_app.user_list[0]['name']
			password = cars_app.user_list[0]['password']
			self.assertEqual("admin",
			                 cars_app.user_list[0]['perm'])

		with allure.step("Send GET request"):
			response = requests.get(self.URL, auth=(username,
			                                        password))

		with allure.step("Verify status code"):
			self.assertEqual(200,
			                 response.status_code)

		with allure.step("Verify 'successful' flag"):
			self.assertTrue(response.json()['successful'])

		with allure.step("Verify retrieved cars list"):
			self.assertListEqual(self.CARS_LIST,
			                     response.json()['cars_list'])

	def test_get_list_of_cars_non_admin(self):
		"""
		Get full list of cars using non admin user credentials.
		:return:
		"""

		with allure.step("Verify user permissions"):
			username = cars_app.user_list[1]['name']
			password = cars_app.user_list[1]['password']
			self.assertEqual("non_admin",
			                 cars_app.user_list[1]['perm'])

		with allure.step("Send GET request"):
			response = requests.get(self.URL, auth=(username,
			                                        password))

		with allure.step("Verify status code"):
			self.assertEqual(200,
			                 response.status_code)

		with allure.step("Verify 'successful' flag"):
			self.assertTrue(response.json()['successful'])

		with allure.step("Verify retrieved cars list"):
			self.assertListEqual(self.CARS_LIST,
			                     response.json()['cars_list'])

	def test_get_list_of_cars_non_admin_sedan(self):
		"""
		Get full list of cars from type = 'sedan'
		using non admin user credentials.
		:return:
		"""

		with allure.step("Verify user permissions"):
			username = cars_app.user_list[1]['name']
			password = cars_app.user_list[1]['password']
			self.assertEqual("non_admin",
			                 cars_app.user_list[1]['perm'])

		with allure.step("Send GET request"):
			response = requests.get(self.URL + '/filter/sedan',
			                        auth=(username, password))

		with allure.step("Verify status code"):
			self.assertEqual(200,
			                 response.status_code)

		with allure.step("Verify retrieved cars list"):
			self.assertListEqual(self.CARS_SEDAN,
			                     response.json()['cars'])

	def test_get_list_of_cars_admin_hatchback(self):
		"""
		Get full list of cars from type = 'hatchback'
		using admin user credentials.
		:return:
		"""

		with allure.step("Verify user permissions"):
			username = cars_app.user_list[0]['name']
			password = cars_app.user_list[0]['password']
			self.assertEqual("admin",
			                 cars_app.user_list[0]['perm'])

		with allure.step("Send GET request"):
			response = requests.get(self.URL + '/filter/hatchback',
			                        auth=(username, password))

		with allure.step("Verify status code"):
			self.assertEqual(200,
			                 response.status_code)

		with allure.step("Verify retrieved cars list"):
			self.assertListEqual(self.CARS_HATCHBACK,
			                     response.json()['cars'])

	def test_get_car_by_name_non_admin_swift(self):
		"""
		Get car data by name = 'swift'
		using non admin user credentials.
		:return:
		"""

		with allure.step("Verify user permissions"):
			username = cars_app.user_list[1]['name']
			password = cars_app.user_list[1]['password']
			self.assertEqual("non_admin",
			                 cars_app.user_list[1]['perm'])

		with allure.step("Prepare expected results"):
			car = {"brand": "Maruti",
			       "car_type": "hatchback",
			       "name": "Swift",
			       "price_range": "3-5 lacs"}

		with allure.step("Send GET request"):
			response = requests.get(self.URL + '/Swift',
			                        auth=(username, password))

		with allure.step("Verify status code"):
			self.assertEqual(200,
			                 response.status_code)

		with allure.step("Verify 'successful' flag"):
			self.assertTrue(response.json()['successful'])

		with allure.step("Verify retrieved car data"):
			self.assertDictEqual(car,
			                     response.json()['car'])
