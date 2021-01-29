from threading import Thread
from time import sleep


def print_cube(num):
    """
    function to print cube of given num
    """
    sleep(3)
    print("Cube: {}".format(num * num * num))


def print_square(num):
    """
    function to print square of given num
    """
    sleep(3)
    print("Square: {}".format(num * num))


if __name__ == "__main__":
    # creating thread
    t1 = Thread(target=print_square, args=(10,))
    t2 = Thread(target=print_cube, args=(10,))

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
    # Hello gets printed in the output even though t1 and t2 were not completed
    # hence proving that these threads are running asynchronously
    print('Hello')

    # wait until thread 1 is completely executed
    t1.join()
    # wait until thread 2 is completely executed
    t2.join()

    # both threads completely executed
    print("Done!")
