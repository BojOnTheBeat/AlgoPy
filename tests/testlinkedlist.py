import sys
import os
import unittest
sys.path.append('..')
try:  # surround import with try/except to get rid of pep8 complaint
    from data_structures.linkedlist import *
except:
    raise


if __name__ == '__main__':
    a = Node(1, Node(2, Node(3)))

    ll = LinkedList(a)

    print(ll) # 123

    #a = ll.reverse()
    print(ll) #123
    print(ll.reverse()) #321
    print(ll)
    print(ll.reverse())

    ll.prepend(8)
    print(ll)
    print(ll.reverse())

