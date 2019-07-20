import logging
import argparse

# assuming loglevel is bound to the string value obtained from the
# command line argument. Convert to upper case to allow the user to
# specify --log=DEBUG or --log=debug
LOG_LEVEL = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
USER_CHOICE = LOG_LEVEL+list(map(lambda w: w.lower(), LOG_LEVEL))


def set_parser_args(parser):
    parser.add_argument("--log", help='set log level',
                        choices=USER_CHOICE,
                        default="WARN")


def parse_arguments():
    parser = argparse.ArgumentParser()
    set_parser_args(parser)
    return parser.parse_args()


def main():
    args = parse_arguments()
    # parse log level
    numeric_level = getattr(logging, args.log.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % loglevel)
    logging.basicConfig(level=numeric_level)
    
    logger = logging.getLogger(__name__)
    # code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == '__main__':
    main()
