#!/path/to/interpreter

"""Helper Class"""


class Helper:
	"""
	Helper Class.
	Contains helper methods for cars_app app
	"""

	@staticmethod
	def check_auth(username, password, user_list):
		"""
		check if the given is valid
		:param user_list:
		:param username:
		:param password:
		:return:
		"""

		user = [user for user in user_list if user['name']
		        == username and user['password'] == password]
		if len(user) == 1:
			return True
		return False
