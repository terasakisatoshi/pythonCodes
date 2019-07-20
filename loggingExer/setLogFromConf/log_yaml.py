import logging
import logging.config
import yaml  # conda install pyyaml

def main():
    logging.config.dictConfig(yaml.load(open("tutorial.yaml").read()))
    # create logger
    logger = logging.getLogger('simpleExample')
    # 'application' code
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == '__main__':
    main()