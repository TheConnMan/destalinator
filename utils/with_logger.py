import logging
import sys


class WithLogger(object):
    @property
    def logger(self):
        logger = logging.getLogger(type(self).__name__)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(formatter)
        logger.addHandler(ch)
        return logger
