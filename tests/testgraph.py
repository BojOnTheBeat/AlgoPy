import sys
import os
import unittest
sys.path.append('..')
try:  # surround import with try/except to get rid of pep8 complaint
    from data_structures.graph import *
except:
    raise


if __name__ == '__main__':

    g = Graph('undirected')
    g.addEdge(1, 2)
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(2, 3)
    print(g.getEdges())
    print(g.getNodes())
    print(g.getDegrees())

    print(g.getDegree(1))
    print(g)

