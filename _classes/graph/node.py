__author__ = 'Soroush'

import networkx as nx


class Node(nx.Node):
    def __init__(self, color):
        """
        :return:
        """
        self.color = color

    def energy(self):
        """
        calculate energy of node. energy of node is the number of it's neighbors with a different color.
        :return:
        """
        return self.neighbors_count() - self.neighbors_count(self.color)

    def neighbors(self, color = None):
        """
        get array of neighbors of this node with specific color. referred as N_p(c) in the paper.
        :param color:
        :return:
        """
        # TODO: get neighbors of this node
        neighbors = self.get_neighbors
        required = []

        for neighbor in neighbors:
            if color is None:
                required.append(neighbor)
            elif neighbor.color.is_equal_to(color):
                required.append(neighbor)

        return required

    def neighbors_count(self, color = None):
        """
        get number of neighbors with this color.
        :param color:
        :return:
        """
        return len(self.neighbors(color))

    def select_candidate_nodes(self, selecting_type = CANDIDATE_OPTIONS.LOCAL, random_sample = None):
        """
        TODO
        :param random_sample:
        :param selecting_type:
        :return:
        """
        pass

    def find_swap_partner(self):
        """
        TODO: find the best node as swap partner for this node.
        :return:
        """
        self.select_candidate_nodes()
        pass
