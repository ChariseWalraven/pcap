# Scenario

# As you already know, a stack is a data structure realizing the LIFO (Last In – First Out) model. It's easy and you've
# already grown perfectly accustomed to it.

# Let's try something new now. A queue is a data model characterized by the term FIFO: First In – First Out. Note: a
# regular queue (line) you know from shops or post offices works exactly in the same way – a customer who came first
# is served first too.

# Your task is to implement the Queue class with two basic operations:

# put(element), which puts an element at end of the queue;
# get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to
# successfully perform it.)

# Follow the hints:

# use a list as your storage (just like we did with the stack)
# put() should append elements to the beginning of the list, while get() should remove the elements from the end of the
# list;
# define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to
# operate on an empty list.


class QueueError(LookupError):  # LookupError because in this case the queue doesn't exist
    "Raised when the queue doesn't exist"
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        pass

    def get(self):
        pass


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except QueueError as e:
    print("Queue error", e)
except BaseException as e:
    print('Whoops! Something funny happened.', e)

# Expected output:
# 1
# dog
# False
# Queue error
