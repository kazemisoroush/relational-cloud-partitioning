__author__ = 'Soroush'


class JabeJa(object):
    """
    Balanced graph partitioning refers to the problem of partitioning the
    graph into equal-sized components. In this algorithm, each node of
    the graph is a processing unit, with `local` information about
    it's neighbor nodes, and small sub-set of random nodes in
    the graph. We need to minimize the graph energy.
    """

    def __init__(self):
        """
        :return:
        """
        # int number_of_partitions
        # float temperature = 1.5
        # float temperature_delta = .003
        # enum message_types = {INFO, ACK, NACK, SWAP}
        self.partitions = []

    def partition(self, graph, partition_count):
        """
        TODO: main partitioning algorithm.
        :param graph:
        :param partition_count:
        :return:
        """
        return self.partitions

    def find_best_partner(self):
        """
        TODO: find the best node as swap partner for node p
        :return:
        """
        return None
