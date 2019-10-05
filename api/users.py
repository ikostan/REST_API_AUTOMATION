#!/path/to/interpreter

"""Users Class"""


class Users:
	"""
	Contains Users data set
	"""

	USER_LIST = [{"name": "qxf2",
	              "password": "qxf2",
	              "perm": "admin"},
	             {"name": "eric",
	              "password": "testqxf2",
	              "perm": "non_admin"},
	             {"name": "morgan",
	              "password": "testqxf2",
	              "perm": "non_admin"},
	             {"name": "jack",
	              "password": "qxf2",
	              "perm": "non_admin"}]

	def get_users(self):
		"""
		Returns users list
		:return:
		"""
		return self.USER_LIST
