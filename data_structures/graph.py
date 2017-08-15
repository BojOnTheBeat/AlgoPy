"""
Python implementation of a Graph.
Using adjacency list implememtation
"""
from collections import defaultdict


class Graph(object):
    """
    Adjacenty list implentation of a graph.
    By default this graph is undirected
    """
    def __init__(self, directedOrUndirected='undirected'):
        self.graph = defaultdict(list)
        self.directedOrUndirected = directedOrUndirected

    def __str__(self):
        """
        string representation of a graph data structure
        TODO: change this to a more intuitive representation
        """
        stringRepresentation = []
        for node in self.getNodes():
            stringRepresentation.append("->".join(
                (str(node), str(self.graph[node]))))

        return str(stringRepresentation)

    def getNodes(self):
        """
        return a list of the nodes in the graph
        """
        return self.graph.keys()

    def getEdges(self):
        """
        return a list of the edges in this graph
        """
        # for node in graph,
        # return node -> node for j in graph[node]

        return ["->".join([str(n1), str(n2)]) for n1 in self.graph.keys() for n2 in self.graph[n1]]

    def addEdge(self, startNode, endNode):
        """
        Add an edge to the graph
        """
        if self.directedOrUndirected == 'undirected':
            # no need to check if edge already exists because we're using
            # defaultdict

            self.graph[startNode].append(endNode)
            self.graph[endNode].append(startNode)
        else:
            self.graph[startNode].append(endNode)

    def addNode(self, newNode):
        """
        Add a singleton node to the graph
        """
        if newNode not in self.graph.keys():
            self.graph[newNode] = []

    def getDegrees(self):
        """
        Return the number of incident degrees per node

        Returns a tuple (a, b) where a is the node and b is the
        degree
        """
        l = []
        for node in self.getNodes():
            l.append((node, len(self.graph[node])))

        return l

    def getDegree(self, node):
        """
        Get the degree of a specific node in the graph
        """

        return len(self.graph[node])

    # detect cycle in undirected
    # detect cycle in directed
    # bfs
    # dfs
    # topological sort
    # dijkstra
    # longest path in a DAG
    # shortest path
    # Assign direction to edges so that the DAG remains acyclic






