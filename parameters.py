class CANDIDATE_OPTION:
    """
    three possible ways of selecting the candidate set.
    """
    LOCAL = 1
    RANDOM = 2
    HYBRID = 3

    def __init__(self):
        pass


class MESSAGE_TYPES:
    """
    messages that can pass between graph vertices.
    """
    INFO = 1
    ACK = 2
    NACK = 3
    SWAP = 4

    def __init__(self):
        pass


ALPHA = 1
"""
parameter of energy.
"""

TEMPERATURE = 1.5
"""
temperature variable for simulated annealing technique.
"""

TEMPERATURE_DELTA = .003
"""
temperature will decrease at each step by this parameter.
"""
