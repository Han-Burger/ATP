import logging
import os

class Logger(object):
    def __init__(self, name):
        logger = logging.getLogger('atp.{0}'.format(name))
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            file_name = os.path.join(os.path.dirname(__file__), 'log.log')
            fh = logging.FileHandler(file_name)
            fmt = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s')
            fh.setFormatter(fmt)
            fh.setLevel(logging.DEBUG)
            logger.addHandler(fh)
        self._logger = logger

    def get(self):
        return self._logger


if __name__ == "__main__":
    logger = Logger('test_module').get()
    logger.debug('haha')