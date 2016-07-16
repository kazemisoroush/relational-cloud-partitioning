from _classes.graph import config
from _classes.graph.color import Color


class Node:
    def __init__(self, color, graph):
        """
        :return:
        """
        self.color = Color(color)
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

    def select_candidate_nodes(self, selecting_type = config['CANDIDATE_OPTIONS']['LOCAL'], random_sample = None):
        """
        decide which sampling option should be done.
        :param random_sample:
        :param selecting_type:
        :return:
        """
        if selecting_type == config['CANDIDATE_OPTIONS']['RANDOM']:
            return self.sample_randomly(random_sample)
        elif selecting_type == config['CANDIDATE_OPTIONS']['HYBRID']:
            return self.sample_hybridly(random_sample)
        else:
            return self.sample_locally()

    def sample_randomly(self, random_sample = None):
        """
        TODO: every node should select a uniform random sample of the nodes in the graph.
        :return:
        """
        pass

    def sample_hybridly(self, random_sample = None):
        """
        TODO: in this policy first the immediate neighbor nodes are selected (i.e., the local policy). If this selection
        fails to improve the pair-wise utility, the node is given another chance for improvement, by letting it to
        select nodes from its random sample (i.e., the random policy).
        :return:
        """
        pass

    def sample_locally(self):
        """
        every node should consider it's directly connected neighbors for color exchange.
        :return:
        """
        return self.neighbors()

    def find_swap_partner(self):
        """
        find the best node as swap partner for this node.
        :return:
        """
        best_utility = 0
        best_partner = None
        alpha = config['PARTITIONING']['ALPHA']
        temperature = config['PARTITIONING']['TEMPERATURE']

        for q in self.select_candidate_nodes():
            d_pp = self.neighbors_count(self.color)
            d_qq = q.neighbors_count(q.color)

            d_pq = self.neighbors_count(q.color)
            d_qp = q.neighbors_count(self.color)

            old_utility = d_pp ** alpha + d_qq ** alpha
            new_utility = d_pq ** alpha + d_qp ** alpha

            if (new_utility * temperature > old_utility) or (new_utility > best_utility):
                best_partner = q
                best_utility = new_utility

        return best_partner

    def __str__(self):
        return str(self.color)
