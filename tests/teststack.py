import sys
import os
import unittest
sys.path.append('..')
try:  # surround import with try/except to get rid of pep8 complaint
    from data_structures.stack import *
except:
    raise


class TestStack(unittest.TestCase):
    def test_stack(self):
        my_stack = Stack([1, 2, 3])




if __name__ == '__main__':
    a = Stack([1, 2, 3])
    print(a)
