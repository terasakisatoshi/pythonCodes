import logging
import threading
import time

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

def worker():
    #logging.debug('starging')
    time.sleep(2)
    print("hoge")
    #logging.debug('exiting')

def my_service():
    logging.debug("starting")
    time.sleep(3)
    logging.debug("exiting")


w2=threading.Thread(name=worker)
w3=threading.Thread(name=worker)

w3.start()
w2.start()