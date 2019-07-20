import logging
import time
def main():
    while True:
        time.sleep(1)
        logging.warn('hello')
    
if __name__ == '__main__':
    main()