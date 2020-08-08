import logging
import os

logging.basicConfig(
     level=os.environ.get("LOG_LEVEL", "DEBUG"),
     format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
     datefmt='%H:%M:%S'
 )
