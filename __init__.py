import configparser
import random
from random import randint

from _classes.graph.graph import Graph
from _classes.graph.node import Node


def main():
    # get application's configurations...
    config = configparser.ConfigParser()
    config.read('configurations.ini')

    node_count = int(config['graph']['NUMBER_OF_NODES'])
    color_count = int(config['graph']['NUMBER_OF_COLORS'])
    neighbor_count = int(config['graph']['NUMBER_OF_NEIGHBORS'])

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

        # make a sample data and build the corresponding graph randomly...

        # start the timer...
        # load the big table
        # make graph model for attributes
        # partition the attribute list with ja-be-ja algorithm
        # make data chunks
        # make the graph model with data chunks and queries
        # partition graph with ja-be-ja algorithm
        # stop the timer...


if __name__ == "__main__":
    main()
