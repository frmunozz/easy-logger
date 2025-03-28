import os
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
from dotenv import load_dotenv
load_dotenv(os.path.join(base_path, ".env.example"))

from elogger import create_logger, LoggerMixin
from elogger.consts import DEFAULT_LOGFILE

"""
we can create a logger directly with the create_logger() function
"""

DEMO_LOG_FOLDER = os.path.join(base_path, "demo", "logs")

logger = create_logger("example", log_folder=DEMO_LOG_FOLDER)

logger.info("testing logger")
logger.debug("we are on debug mode also")
logger.debug("the logfile env option is: %s", DEFAULT_LOGFILE)


"""
we can also create a class with an integrated logger using the logger mixin
"""

class TestingLogger(LoggerMixin):
    _log_folder = DEMO_LOG_FOLDER
    _log_file = "class_example.log"

    def test_logger(self):
        self.logger.info("testing logger")
        self.logger.debug("we are on debug mode also")
        self.logger.debug("the logfile env option is: %s", DEFAULT_LOGFILE)



x = TestingLogger()
x.test_logger()