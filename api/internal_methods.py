#!/path/to/interpreter

"""REST API app internal methods"""

from functools import wraps
from data import TestData
from flask import request, jsonify


def check_auth(username, password):
    """
    Check if the given is valid
    :param username:
    :param password:
    :return: True/False
    """
    user = [user for user in TestData.USER_LIST if user['name']
            == username and user['password'] == password]
    if len(user) == 1:
        return True

    return False


def authenticate_error(auth_flag):
    """
    Set auth message based on the authentication check result
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


def requires_auth(f):
    """
    Verify given user authentication details
    :param f:
    :return:
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        """
        Decorated function
        :param args:
        :param kwargs:
        :return:
        """
        auth = request.authorization
        auth_flag = True

        if not auth:
            auth_flag = False
            return authenticate_error(auth_flag)
        elif not check_auth(auth.username, auth.password):
            return authenticate_error(auth_flag)
        return f(*args, **kwargs)

    return decorated


def requires_perm():
    """
    Check if the authenticated user has a admin permission
    :return: permission flag True/False
    """
    auth = request.authorization
    perm_flag = False
    for user in TestData.USER_LIST:
        if user['name'] == auth.username and user['perm'] == 'admin':
            perm_flag = True
            return perm_flag

    return perm_flag
