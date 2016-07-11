import configparser


def main():
    config = configparser.ConfigParser()
    config.read('configurations.ini')
    print(config['partitioning']['SWAP'])
    # parse configurations...
    # parse parameters...

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
