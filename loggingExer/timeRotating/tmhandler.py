import logging
from logging.handlers import TimedRotatingFileHandler

logfile_name = 'timerot.log'

log_fmt = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(format=log_fmt)
# logger setting
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logHandler = TimedRotatingFileHandler(logfile_name, when='S')
logHandler.setFormatter(logging.Formatter(log_fmt))
logger.addHandler(logHandler)
# code
logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')
