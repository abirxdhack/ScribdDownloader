# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import logging
from logging.handlers import RotatingFileHandler

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s", 
    datefmt='%Y-%m-%d %H:%M:%S',  
    handlers=[
        RotatingFileHandler(
            "botlog.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("aiohttp").setLevel(logging.ERROR)  
logging.getLogger("apscheduler").setLevel(logging.ERROR)

LOGGER = logging.getLogger(__name__)