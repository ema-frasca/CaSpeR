

import os
import string
import random


def create_if_not_exists(path: str) -> None:
    """
    Creates the specified folder if it does not exist.
    :param path: the complete path of the folder to be created
    """
    if not os.path.exists(path):
        os.makedirs(path)


def random_id(length=8, alphabet=string.ascii_letters+string.digits ):
    return ''.join(random.choices(alphabet, k=length))
