__author__ = 'Soroush'

import networkx as nx


class Graph(nx.Graph):
    def __init__(self):
        """
        :return:
        """
        pass

    def energy(self):
        """
        Calculate graph's energy. (is equal to sum of energy of all nodes)
        :return:
        """
        nodes = self.nodes()
        energy = 0

        for node in nodes:
            energy += node.energy()

        return energy