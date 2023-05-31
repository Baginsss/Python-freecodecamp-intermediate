import logging as log

logger = log.getLogger(__name__)
logger.propagate = False
logger.info('Hello from helper')

# create handler
handler = log.StreamHandler()
file_handler = log.FileHandler('file.log')

# level and the format of the handler
handler.setLevel(log.WARNING)
file_handler.setLevel(log.ERROR)

stream_format = log.Formatter('%(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(stream_format)
handler.setFormatter(stream_format)

# add handler to the logger
logger.addHandler(handler)
logger.addHandler(file_handler)

logger.warning('This is a warning message')
logger.error('This is an error message')

