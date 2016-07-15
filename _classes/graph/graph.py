import networkx as nx


class Graph(nx.Graph):
    def __init__(self):
        """
        Instantiate the NetworkX super graph object.
        :return:
        """
        super(Graph, self).__init__()

    def energy(self):
        """
        calculate graph's energy. the energy of the graph is the sum of the energy of
        the nodes. we count each edge twice, so we divide the result by two.
        :return:
        """
        nodes = self.nodes()
        energy = 0

        for node in nodes:
            energy += node.energy()

        return .5 * energy

    def make_neighbor(self, node, neighbors):
        for neighbor in neighbors:
            self.add_edge(node, neighbor)
