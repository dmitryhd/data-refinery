import logging
import logging.handlers
import os.path as path


LOGGER_NAME = 'refinery'
LOG_FORMAT = '[%(asctime)s] %(levelname)-8s %(message)s'
TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
LOG_DEFAULT_LEVEL = logging.DEBUG


def configure_logger(logger_name=LOGGER_NAME,
                     log_dir='/tmp/',
                     level=LOG_DEFAULT_LEVEL,
                     filename=''):
    """
    Returns logger which output to stdout and and to specified file.
    Example: logger = configure_logger('just_log')
    will output log with timestamps to /var/local/log/just_log.log
    """
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)
    logger.handlers = []

    # Stdout
    stdout = get_stream_handler()
    stdout.setLevel(level)
    logger.addHandler(stdout)

    # Filehandler
    if not filename:
        filename = logger_name + '.log'
    log_location = path.join(log_dir, filename)
    print('Log to file {}'.format(log_location))
    add_file_handler(logger, log_location, level)
    # add_file_handler(logger, log_location + '_no_color', level, color=False)

    logger.propagate = False
    return logger


def get_formatter():
    return logging.Formatter(LOG_FORMAT, TIME_FORMAT)


def get_stream_handler():
    handler = logging.StreamHandler()
    handler.setFormatter(get_formatter())
    return handler


def add_file_handler(logger: logging.Logger, filename: str, level: int):
    file_handler = logging.handlers.RotatingFileHandler(filename, mode='a', maxBytes=10**8, backupCount=3)
    file_handler.setLevel(level)
    file_handler.setFormatter(get_formatter())
    logger.addHandler(file_handler)
