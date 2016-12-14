import logging

from refinery import ModelDataStorage


class Process:
    __logger_fmt = '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

    def __init__(self, storage: ModelDataStorage, logger_name: str = ''):
        self.storage = storage
        self._logger_name = logger_name
        self._setup_logger()

    def _setup_logger(self):
        self.logger = logging.getLogger('{}.{}'.format(self._logger_name, self.__class__.__name__))

        if not len(self.logger.handlers):
            self.logger.addHandler(logging.StreamHandler())

        self.logger.setLevel(logging.INFO)
        for handler in self.logger.handlers:
            handler.setFormatter(logging.Formatter(self.__logger_fmt))


class Downloader(Process):
    def run(self):
        self.logger.info('started')
        self.storage.add_dict({'stopped': True}, 'info')
        self.logger.info('downloader done')


class Trainer(Process):
    def run(self):
        self.logger.info('started')
        self.info = self.storage.get_dict('info')
        self.logger.info('done {}'.format(self.info))
