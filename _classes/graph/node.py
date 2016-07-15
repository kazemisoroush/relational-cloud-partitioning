class Node:
    def __init__(self, color, graph):
        """
        :return:
        """
        self.color = color
        self.graph = graph

    def energy(self):
        """
        calculate energy of node. energy of node is the number of it's neighbors with a different color.
        :return:
        """
        return self.neighbors_count() - self.neighbors_count(self.color)

    def neighbors(self, color = None):
        """
        TODO: get array of neighbors of this node with specific color. referred as N_p(c) in the paper.
        :param color:
        :return:
        """
        neighbors = self.graph.neighbors(self)
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

    def select_candidate_nodes(self, selecting_type = None, random_sample = None):
        """
        decide which sampling option should be done.
        :param random_sample:
        :param selecting_type:
        :return:
        """
        if selecting_type == CANDIDATE_OPTIONS.RANDOM:
            return self.sample_randomly(random_sample)
        elif selecting_type == CANDIDATE_OPTIONS.HYBRID:
            return self.sample_hybridly(random_sample)
        else:
            return self.sample_locally()

    def sample_randomly(self, random_sample = None):
        """
        TODO
        :return:
        """
        pass

    def sample_hybridly(self, random_sample = None):
        """
        TODO
        :return:
        """
        pass

    def sample_locally(self):
        """
        TODO
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

    def __str__(self):
        return str(self.color)
