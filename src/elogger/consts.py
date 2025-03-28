import os

BASE_PATH = os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

LOG_FOLDER = os.environ.get(
    "LOG_FOLDER", os.path.join(BASE_PATH, "logs"))

os.makedirs(LOG_FOLDER, exist_ok=True)

# log levels -> 10=debug, 20=info, 30=warning
LOGLEVEL = int(os.environ.get("LOGLEVEL", "10"))
DEFAULT_LOGFILE = os.environ.get("DEFAULT_LOGFILE", "log.log")
