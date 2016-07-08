class Color(object):
    def __init__(self, label):
        """
        :return:
        """
        self.label = label

    def is_equal_to(self, color):
        """
        check whether this color is equal to input color.
        :param color:
        :return:
        """
        return color.label == self.label
