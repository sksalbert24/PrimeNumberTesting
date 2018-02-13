import time
import logging
from functools import wraps


class Wrapper:
    @staticmethod
    def time_wrapper(func):
        @wraps(func)
        def wrapping(*args, **kwargs):
            t1 = time.time()
            func(*args, **kwargs)
            print(time.time() - t1)
        return wrapping

    @staticmethod
    def log_wrapper(func):
        @wraps(func)
        def wrapping(*args, **kwargs):
            logging.basicConfig(filename='.\\log.log', level=logging.WARNING)
            logger = logging.getLogger()
            logger.warning('logging test: {} ran with parameters {} {}'.format(func.__name__, args, kwargs))
            func(*args, **kwargs)
        return wrapping
