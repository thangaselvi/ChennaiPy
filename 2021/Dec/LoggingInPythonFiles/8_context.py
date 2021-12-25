import sys
import logging

host_ip_addr = "localhost"

class StdoutFilter(logging.Filter):
    def filter(self, record):
        return record.levelno in (logging.INFO, logging.ERROR)

logger = logging.getLogger('sampleApp')
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.addFilter(StdoutFilter())
formatter = logging.Formatter('%(host_ip)s - %(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

logger = logging.LoggerAdapter(logger, {'host_ip': host_ip_addr})
print(logger)

logger.debug('This is a debug from main module')
logger.info('This is a info from main module')
logger.warning('This is a warning from main module')
logger.error('This is an error from main module')
