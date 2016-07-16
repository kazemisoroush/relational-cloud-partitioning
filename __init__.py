import configparser


def main():
    # get application's configurations...
    config = configparser.ConfigParser()
    config.read('configurations.ini')

    node_count = int(config['GRAPH']['NUMBER_OF_NODES'])
    color_count = int(config['GRAPH']['NUMBER_OF_COLORS'])
    neighbor_count = int(config['GRAPH']['NUMBER_OF_NEIGHBORS'])

    # make a sample data and build the corresponding graph randomly...
    graph = GraphData().randomGraph(node_count, color_count, neighbor_count)

    print(graph.energy())

    # start the timer...
    # load the big table
    # make graph model for attributes
    # partition the attribute list with ja-be-ja algorithm
    # make data chunks
    # make the graph model with data chunks and queries
    # partition graph with ja-be-ja algorithm
    # stop the timer...


from _classes.data.graphData import GraphData

if __name__ == "__main__":
    main()
