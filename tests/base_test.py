#!/path/to/interpreter

"""
Base Test Case
"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import os
import platform
import time
import unittest
import allure
from utils.get_args_from_cli import get_args


class BaseTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """
        1. Get Args from CLI
        2. Set Test URL
        3. Start REST API Service
        :return:
        """

        allure.dynamic.title("Test pre set-up")

        with allure.step("Get args from CLI"):
            # cls.args = get_args()
            pass

        with allure.step("Set test URL"):
            cls.URL = 'http://127.0.0.1:5000/cars'

        with allure.step("Start REST API Service"):
            print("\nOS: {}\n".format(platform.system()))

            if platform.system() == 'Windows':
                os.system("start /B start cmd.exe @cmd /k python ../cars_app.py")

            if platform.system() == 'Linux':
                os.system('pkill -f cars_app.py')
                os.system("python3 ../cars_app.py &")
                pass

        time.sleep(5)

    @classmethod
    def tearDownClass(cls) -> None:
        """
        1. Stop REST API Service
        :return:
        """
        allure.dynamic.title("Post test activities")

        with allure.step("Stop REST API Service"):
            if platform.system() == 'Windows':
                # os.system('taskkill /F /IM python.exe')
                pass

            if platform.system() == 'Linux':
                os.system('pkill -f cars_app.py')
                pass
