import threading


class Worker(threading.Thread):
    """
    TODO
    """

    def __init__(self, vertices):
        """
        TODO
        :param vertices:
        """
        super(Worker, self).__init__()
        self.vertices = vertices

    def run(self):
        """
        TODO: start working.
        :return:
        """
        self.superstep()

    def superstep(self):
        """
        TODO: Completes a single superstep for all the vertices in self.
        """
        for vertex in self.vertices:
            if vertex.active:
                vertex.update()
