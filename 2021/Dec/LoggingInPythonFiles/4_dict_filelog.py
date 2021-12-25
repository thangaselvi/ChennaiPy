import logging
import logging.config
import yaml

with open('4_dict_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

logger.debug('This is a debug message')
logger.info('This is a info message')
logger.error('This is a error message')
