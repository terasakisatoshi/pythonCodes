import logging
logging.basicConfig(level='DEBUG', filename='output_logfile.log')

logger=logging.getLogger("bunyan")
logging.debug("where is my axe?")
logging.warn("I need my axe")
