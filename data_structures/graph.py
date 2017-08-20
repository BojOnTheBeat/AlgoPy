"""
Python implementation of a Graph.
Using adjacency list implememtation.
Uses the queue and stack data structures
"""
from collections import defaultdict
from queue import Queue


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

    def getAdjacent(self, node):
        """
        Return a list of all the adjacent nodes to the given node
        """
        return self.graph[node]

    # detect cycle in undirected
    # detect cycle in directed
    # bfs

    def bfs(self, startNode):
        """
        This is a function that performs a Breadth First Search
        On the graph and prints out the order of the search
        """
        queue = Queue()

        # Mark all the nodes as not visited
        visited = {}
        for node in self.getNodes():
            visited[node] = False

        queue.enqueue(startNode)

        while not queue.isEmpty():
            s = queue.dequeue()
            visited[s] = True
            print s,

            # enqueue all the adjacent vertices to s
            # if they've not already been visited

            for adjacentNode in self.getAdjacent(s):
                if visited[adjacentNode] is False:
                    queue.enqueue(adjacentNode)
                    visited[adjacentNode] = True

    # dfs
    # bfs applications
    # dfs applications
    # topological sort
    # dijkstra
    # longest path in a DAG
    # shortest path
    # kruskal(mst)
    # Assign direction to edges so that the DAG remains acyclic
