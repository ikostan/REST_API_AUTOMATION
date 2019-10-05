#!/path/to/interpreter

"""Cars Class"""


class Cars:
	"""
	Contains cars list data
	"""

	CARS_LIST = [{"name": "Swift",
	              "brand": "Maruti",
	              "price_range": "3-5 lacs",
	              "car_type": "hatchback"},
	             {"name": "Creta",
	              "brand": "Hyundai",
	              "price_range": "8-14 lacs",
	              "car_type": "hatchback"},
	             {"name": "City",
	              "brand": "Honda",
	              "price_range": "3-6 lacs",
	              "car_type": "sedan"},
	             {"name": "Vento", "brand":
		             "Volkswagen",
	              "price_range": "7-10 lacs",
	              "car_type": "sedan"}]

	def get_cars(self):
		"""
		Returns cars list data
		:return:
		"""
		return self.CARS_LIST
