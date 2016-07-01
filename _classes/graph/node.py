__author__ = 'Soroush'

import networkx as nx
# from _classes.graph.color import Color


class Node(nx.Node):
    def __init__(self, color):
        """
        :return:
        """
        self.color = color
        pass

    def energy(self):
        """
        TODO: calculate energy of node.
        :return:
        """
        return 0

    def neighboars(self, color=None):
        """
        TODO: get array of neighbors of this node.
        :param color:
        :return:
        """
        if color is None:
            # get all neighbors.
            return []

        # get (color = color) neighbors.
        return []