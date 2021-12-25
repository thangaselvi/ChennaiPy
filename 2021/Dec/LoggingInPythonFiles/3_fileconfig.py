###
# Creating a logging config file and reading it using the fileConfig() function.
# In the below example:
# 	Created a logger with the 'simpleExample' logger name.
# 	Create a console handler with the debug level set, and file handler with info level set hence the debug log will not be printed
# 	Both the configurations are taken from the logging.conf file
# 	Its important to have the handler and logger set for 'root'
# In file handler:
# 	The propagate entry is set to 1 to indicate that messages must propagate to handlers higher up the logger hierarchy from this logger, or 0 to indicate that messages are not propagated to handlers up the hierarchy. 
# 	The qualname entry is the hierarchical channel name of the logger, that is to say the name used by the application to get the logger.
# FileRotateHandler
# 	Here we have used file rotate handler, to avoid logging all the content in a single huge file
# 	We have configured maxBytes=10, about 10bytes written the will be rotated
# 	backupcount=5, it says how many rotated files needs to be kept rest will be cleaned.
# 	Create formatter with time, module name, level and message 
###
import logging
import logging.config

logging.config.fileConfig('3_logging.conf')

# create logger
logger1 = logging.getLogger('simpleExample')
logger = logging.getLogger()

# 'application' code
logger.debug('debug message')
logger1.info('info message')
logger1.warning('warn message')
logger1.error('error message')
logger1.critical('critical message')
