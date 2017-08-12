"""
Python implementation of a LinkedList.

"""


class Node(object):
    def __init__(self, obj, next=None):
        self.obj = obj
        self.next = next


class LinkedList(object):
    def __init__(self, node=None):
        self.head = node
    
    



