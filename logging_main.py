import logging as log
import logging.config
import traceback
from logging.handlers import RotatingFileHandler
from logging.handlers import TimedRotatingFileHandler
import time

# basicconfig is used to configure the logging system
# log.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                 datefmt='%Y/%m/%d %H:%M:%S', level=log.DEBUG)

# log.debug('This is a debug message')
#log.info('This is an info message')
#log.warning('This is a warning message')
#log.error('This is an error message')
#log.critical('This is a critical message')


# logging.config.fileConfig('logging.conf')

# logger = log.getLogger('simpleExample')
# logger.debug('This is a debug message')

try:
    a = [1, 2, 3]
    val = a[4]
# except IndexError as e:
#     logging.error(e, exc_info=True)
except:
    logging.error('The error is %s', traceback.format_exc())

logger = log.getLogger(__name__)
logger.setLevel(log.INFO)

handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
logger.addHandler(handler)

for _ in range(10):
    logger.info('Hello, world!')

# s, m, h, d, midnight, w0
handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
logger.addHandler(handler)

for _ in range(6):
    logger.info('Hello, world!')
    time.sleep(5)
