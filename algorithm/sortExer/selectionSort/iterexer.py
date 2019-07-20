import logging
logging.basicConfig(level=logging.INFO)


def iterator():
    for i in range(10):
        yield i

myiter = iterator()
print(myiter.__next__())
print(myiter.__next__())

logging.info("Hello")
