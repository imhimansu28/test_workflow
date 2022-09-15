import logging
import logging.handlers
import os

import requests
from dotenv import load_dotenv

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.getenv('63aac99600695f5cfc14fd3364785c5b')
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    # raise

a = 9
b = 9

if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get(
        'https://github.com/')
    if r.status_code == 200:
        user_name = r.json()[0]['login']
        logger.info(f"User name: {user_name}")
    if a == b:
        logger.info("a is equal to b")
