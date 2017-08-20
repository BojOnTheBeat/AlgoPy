"""
Python implementation of a stack.

"""


class Stack(object):
    def __init__(self, stack=None):
        if stack:
            self.stack = stack
        else:
            self.stack = []

    def __str__(self):
        return ' '.join([str(i) for i in self.stack])

    def push(self, item):
        """
        push an item to the stack
        """
        self.stack.append(item)

    def pop(self):
        """
        pop and return item from the stack. Returns None if stack is empty
        """
        if self.stack:
            return self.stack.pop()
        return None

    def isEmpty(self):
        """check if the stack is empty"""
        return len(self.stack) == 0

    def size(self):
        """check the size of the stack"""
        return len(self.stack)

    def extend(self, lst):
        """
        Extend the stack
        """
        self.stack.extend(lst)







