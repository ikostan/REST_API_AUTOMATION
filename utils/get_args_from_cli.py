#!/path/to/interpreter

"""Extract arguments from CLI"""

#  Created by Egor Kostan.
#  GitHub: https://github.com/ikostan
#  LinkedIn: https://www.linkedin.com/in/egor-kostan/

import sys


def get_args():
    """
    Reads arguments from CLI and returns them as dictionary.
    Helps running Python unittest with command-line arguments.
    Raises Exception if one of the required arguments is missing.
    :return:
    """

    env = None

    for param in sys.argv:

        # Test environment (mainly for web testing)
        if '--env=' in param:
            env = str(param).replace('--env=', '')
            print("\n--env={}".format(env))

    return {'env': env}
