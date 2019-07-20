from logging import getLogger

logger = getLogger(__name__)


def do_something():
    logger.debug("debugging...")
    logger.info("tell information")
    logger.warn("warn it comes from something like ...")
    logger.error("Ops some error is occured")
    logger.critical("critical event happened")
    logger.debug("It's raining again")
    logger.info("with hail the size of hailstones")
