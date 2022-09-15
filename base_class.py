import logging


class BaseClass:

    def getLogger(self):
        logger = logging.getLogger(__name__)
        file_handler = logging.FileHandler('debug.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.CRITICAL)
        return logger
