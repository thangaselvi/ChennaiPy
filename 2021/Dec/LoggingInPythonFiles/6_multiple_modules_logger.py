import sys
import logging
import sub_app 

# Create a custom logger with "test_app"
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Create handlers
# create console handler with debug log level
c_handler = logging.StreamHandler(sys.stdout)

# create file handler with error log level
f_handler = logging.FileHandler('file.log', 'w')
f_handler.setLevel(logging.WARNING)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

print(c_handler)
print(logger)

logger.debug('This is a debug from main module')
logger.info('This is a info from main module')
logger.warning('This is a warning from main module')
logger.error('This is an error from main module')

logger.info("Before calling the sub_app_function")
sub_app.sub_app_function()
logger.info("After calling the sub_app_function")
