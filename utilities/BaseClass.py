import inspect
import logging

import pytest


@pytest.mark.usefixtures('setup')
class BaseClass:
    pass
    # def getLogger(self):
    #     func_name = inspect.stack()[1][3]
    #     logger = logging.getLogger(func_name)
    #     file_handler = logging.FileHandler('debug.log')
    #     formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    #     file_handler.setFormatter(formatter)
    #
    #     logger.addHandler(file_handler)  # filehandler object
    #
    #     logger.setLevel(logging.DEBUG)
    #     return logger


