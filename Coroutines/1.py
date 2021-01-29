def print_name(prefix):
    print("Printing for prefix : {}".format(prefix))
    try:
        while True:
            name = (yield)
            print(prefix + " " + name)
    except GeneratorExit:
        print("Closing coroutine!!")


# Initializing the coroutine
corou = print_name("Dear")
corou.__next__()
# Sending data and control
corou.send("Atul")
corou.send("Aloo")
# Closing coroutine
corou.close()
