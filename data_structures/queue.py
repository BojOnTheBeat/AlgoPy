"""
Python implementation of a queue.

"""


class Queue(object):
    def __init__(self, queue=None):
        if queue:
            self.queue = queue
        else:
            self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        return self.queue.pop()

    def isEmpty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)
