import random
from random import randint
from _classes.graph.graph import Graph
from _classes.graph.node import Node


class GraphData(object):
    def __init__(self):
        """
        :return:
        """
        pass

    @staticmethod
    def randomGraph(node_count, color_count, neighbor_count):
        """
        get a randomly created graph.
        :param node_count:
        :param color_count:
        :param neighbor_count:
        :return:
        """
        graph = Graph()

        # randomly make the nodes and color them.
        for i in range(0, node_count - 1):
            graph.add_node(Node(randint(0, color_count - 1), graph))

        # randomly make neighbors.
        for node in graph.nodes():
            # get all nodes of graph and store it in an array
            other_nodes = graph.nodes()
            # remove current node from that array
            other_nodes.remove(node)
            # randomly choose some nodes from that array
            neighbors = random.sample(other_nodes, randint(0, neighbor_count - 1))
            # loop on the second array and make them neighbors
            graph.make_neighbor(node, neighbors)

        return graph
