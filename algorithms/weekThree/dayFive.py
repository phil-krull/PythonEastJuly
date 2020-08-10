class CirQueue:
    def __init__(self, capacity):
        self.cap = capacity
        self.front = 0
        self.back = 0
        self.size = 0
        self.data = [None] * self.cap

    def is_full(self):
        pass

    def is_empty(self):
        pass

    def enqueue(self, value):
        # add value to queue
        pass

    def dequeue(self):
        # remove and return value in queue
        pass

my_c_q = CirQueue(4)
print(my_c_q.cap)
print(my_c_q.data)
