###
# Filter can be used for both at the logger level or by handler level.
# Such as they can stop certain information to be passed to be logger
# Also inject additional information into the LogRecord which will be logged
# In our below example, we are using filter to allow only certain levels to be logged.
# Though the log level is set to DEBUG, we are only allowing INFO and ERROR to be logged.
###
import sys
import logging

host_ip = "localhost"

class StdoutFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.INFO, logging.ERROR)

logger = logging.getLogger('sampleApp')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.addFilter(StdoutFilter())
formatter = logging.Formatter('{host_id: %(host_ip)s} - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger = logging.LoggerAdapter(logger, {'host_ip': host_ip})
print(logger)

logger.debug('This is a debug from main module')
logger.info('This is a info from main module')
logger.warning('This is a warning from main module')
logger.error('This is an error from main module')
logger.exception('This is an error from main module')

