# For more clarity on below code read this ->
# https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python

from threading import Thread
from queue import Queue


def producer(q):
    for i in range(5):
        q.put(i)
        print("Published", i)


def consumer(q):
    while True:
        data = q.get()
        print("Consumed", data)
        if data == 4:
            break


q = Queue()
producer_thread = Thread(target=producer, args=(q,))
consumer_thread = Thread(target=consumer, args=(q,))
producer_thread.start()
consumer_thread.start()
producer_thread.join()
consumer_thread.join()
