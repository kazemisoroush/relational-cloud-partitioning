class JabeJa(object):
    """
    Balanced graph partitioning refers to the problem of partitioning the
    graph into equal-sized components. In this algorithm, each node of
    the graph is a processing unit, with `local` information about
    it's neighbor nodes, and small sub-set of random nodes in
    the graph. We need to minimize the graph energy.
    """

    def __init__(self, partition_count):
        """
        :return:
        """
        # initialize some public variables:
        self.partition_count = partition_count
        self.partitions = []

    def run(self, graph, partition_count):
        """
        TODO: main partitioning algorithm.
        :param graph:
        :param partition_count:
        :return:
        """
        # 1. initialize node colors uniformly with `self.number_of_partitions`.
        # 2. each node iteratively selects another node from it's neighbors or a random sample.
        #   3. if the color exchange decreases the energy, then swap happens. otherwise, they preserve their colors.
        #   4.
        return self.partitions
