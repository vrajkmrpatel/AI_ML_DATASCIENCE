# import logging

# # Set up basic configuration
# logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# # Creating a logger
# logger = logging.getLogger(__name__)

# # Example usage of different log levels
# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')

# import logging

# # Create a logger
# logger = logging.getLogger('my_logger')
# logger.setLevel(logging.DEBUG)

# # Create file handler to log messages to a file
# file_handler = logging.FileHandler('PythonCodes/app.log')
# file_handler.setLevel(logging.DEBUG)

# # Create a formatter and set it for the handler
# formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
# file_handler.setFormatter(formatter)

# # Add the file handler to the logger
# logger.addHandler(file_handler)

# # Log some messages
# logger.debug('Debug message')
# logger.info('Info message')


import logging

logging.basicConfig(filename="PythonCodes/app.log",
                    format='%(asctime)s %(levelname)s: %(message)s',
                    filemode='a')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Harmless debug message")
logger.info("Just an information")
logger.warning("Its a warning")
logger.error("Did you try to divide by zero?")
logger.critical("Internet is down")