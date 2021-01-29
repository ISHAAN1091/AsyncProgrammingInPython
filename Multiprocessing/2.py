from multiprocessing import Process


def square(num=2):
    for i in range(10000000):
        pass
    print(num**2)


if __name__ == "__main__":
    procs = []
    for i in range(5):
        procs.append(Process(target=square))
    for proc in procs:
        proc.start()
    print('Hello World')
    for proc in procs:
        proc.join()
    num_values = [1, 2, 3, 4]
    for num in num_values:
        proc = Process(target=square, args=(num,))
        procs.append(proc)
        proc.start()
