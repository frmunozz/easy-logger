import logging
import logging.handlers
import types
import os
from .consts import LOG_FOLDER, LOGLEVEL, DEFAULT_LOGFILE



def create_logger(module, loglevel=LOGLEVEL, logfile=DEFAULT_LOGFILE, log_folder=LOG_FOLDER):
    """
    Create a Logger Handler which display messages in format:

    module.ClassName.LevelMessage : textMessage

    code extracted and adapted from:
    https://stackoverflow.com/questions/20111758/how-to-insert-newline-in-python-logging/20156856

    Parameters
    ----------
    module : string
        Name of the module

    logfile : string
        Name of the logging file

    Returns
    -------
    logger : Logger Handler
    """
    # Create a handler
    console_handler = logging.StreamHandler()
    print("using loglevel", loglevel)
    console_handler.setLevel(loglevel)
    console_handler.setFormatter(
        logging.Formatter(
            fmt="[%(asctime)s]:%(name)s.%(funcName)s.%(levelname)s - %(message)s"
        )
    )

    # Create a "blank line" handler
    blank_handler = logging.StreamHandler()
    blank_handler.setLevel(loglevel)
    blank_handler.setFormatter(logging.Formatter(fmt=""))

    # create a file handler
    dirname = os.path.dirname
    filename = os.path.join(log_folder, logfile)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    f_handler = logging.handlers.RotatingFileHandler(filename, maxBytes=10000000, backupCount=5)
    f_handler.setLevel(loglevel)
    f_handler.setFormatter(
        logging.Formatter(
            fmt="[%(asctime)s]:%(name)s.%(funcName)s.%(levelname)s - %(message)s"
        )
    )

    # Create a logger, with the previously-defined handler
    logger = logging.getLogger("{}".format(module))
    logger.setLevel(logging.DEBUG)  # highest level
    logger.addHandler(console_handler)

    # Save some data and add a method to logger object
    logger.console_handler = console_handler
    logger.blank_handler = blank_handler
    logger.addHandler(f_handler)

    return logger


def create_file_logger(module, loglevel=LOGLEVEL, logfile=DEFAULT_LOGFILE, log_folder=LOG_FOLDER, chmod=False):
    # create a file handlerS
    dirname = os.path.dirname
    filename = os.path.join(log_folder, logfile)
    if not os.path.exists(os.path.dirname(filename)):
        os.makedirs(os.path.dirname(filename))
    if chmod:
        # force permissions to write file
        os.system("sudo chmod 777 %s" % filename)
    f_handler = logging.handlers.RotatingFileHandler(filename, maxBytes=10000000, backupCount=5)
    f_handler.setLevel(loglevel)
    f_handler.setFormatter(
        logging.Formatter(
            fmt="[%(asctime)s]:%(name)s.%(funcName)s.%(levelname)s - %(message)s"
        )
    )

    # Create a logger, with the previously-defined handler
    logger = logging.getLogger("{}".format(module))
    logger.setLevel(loglevel)  # highest level
    logger.addHandler(f_handler)

    return logger


class LoggerMixin:
    _logger = None
    _log_level = LOGLEVEL
    _log_file = DEFAULT_LOGFILE
    _log_folder = LOG_FOLDER
    _file_only = False


    @classmethod
    def new_logger(cls):
        """
        Class Method used to modify the class variable, in combination with self.logger(),
        we achive a singleton patter where this variable cls._logger is defined only
        once (the first time) for every instantiation of this class (is shared between
        objects.)

        """
        if cls._file_only:
            cls._logger = create_file_logger(
                cls.__name__, loglevel=cls._log_level, logfile=cls._log_file, log_folder=cls._log_folder
            )
        else:
            cls._logger = create_logger(
                cls.__name__, loglevel=cls._log_level, logfile=cls._log_file, log_folder=cls._log_folder
            )

    @property
    def logger(self) -> logging.Logger:
        """
        Get Logger Handler Using Singleton, the logger will be set only the first time
        is used, then it will use always the same Object instance. This will be shared
        between different instances of this class.

        Returns
        -------
        logger : Logger Handler
        """
        if self._logger is None:
            self.new_logger()
        return self._logger
