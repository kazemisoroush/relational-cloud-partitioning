__author__ = 'Sara'


class Partition(object):
    def __init__(self):
        """
        :return:
        """
        self.nodes = []

    def add_node(self, node):
        """
        add node to partition.
        :param node:
        :return:
        """
        return self.nodes.append(node)

    def get_nodes(self):
        """
        get nodes that appear in this partition.
        :return:
        """
        return self.nodes

    def remove_node(self, node):
        """
        remove node from this partition.
        :param node:
        :return:
        """
        return self.nodes.remove(node)
