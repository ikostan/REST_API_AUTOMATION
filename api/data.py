#!/path/to/interpreter

"""Test data for REST API app"""


class TestData:
    """Test data class for REST API app"""

    CARS_LIST = [{"name": "Swift", "brand": "Maruti",
                  "price_range": "3-5 lacs", "car_type": "hatchback"},
                 {"name": "Creta", "brand": "Hyundai",
                  "price_range": "8-14 lacs", "car_type": "hatchback"},
                 {"name": "City", "brand": "Honda",
                  "price_range": "3-6 lacs", "car_type": "sedan"},
                 {"name": "Vento", "brand": "Volkswagen",
                  "price_range": "7-10 lacs", "car_type": "sedan"}]

    USER_LIST = [{"name": "qxf2", "password": "qxf2", "perm": "admin"},
                 {"name": "eric", "password": "testqxf2", "perm": "non_admin"},
                 {"name": "morgan", "password": "testqxf2", "perm": "non_admin"},
                 {"name": "jack", "password": "qxf2", "perm": "non_admin"}]

    registered_cars = []
