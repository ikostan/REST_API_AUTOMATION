#!/path/to/interpreter

"""Authentication Helper Class"""

from flask import jsonify


class AuthenticationHelper:
	"""
	Authentication Helper Class.
	Contains helper methods for cars_app app
	"""

	@staticmethod
	def check_auth(username, password, user_list):
		"""
		check if the given user is valid
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

	@staticmethod
	def authenticate_error(auth_flag):
		"""
		set auth message based on the
		authentication check result
		:param auth_flag:
		:return:
		"""
		if auth_flag is True:
			message = {'message': "Authenticate with proper credentials"}
		else:
			message = {'message': "Require Basic Authentication"}
		resp = jsonify(message)
		resp.status_code = 401
		resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
		return resp
