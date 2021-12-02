
import logging
class LogginCheck:
    def __init__(self):
        logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(message)s %(asctime)s",
        datefmt='%Y/%m/%d %I:%M:%S %p',
        handlers=[
            logging.FileHandler("debug.log"),
            logging.StreamHandler()
            ]
        )

    def create_info(text):
        logging.info(text)