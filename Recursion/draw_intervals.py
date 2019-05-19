class Ruler:

    def __init__(self, length: int):
        """
        Constructor for a ruler
        :param length: The length of the ruler
        """
        self._length = length


    def draw(self):
        self.draw_interval(self._length // 2)
        self.draw_line()
        self.draw_interval(self._length // 2)

    def draw_interval(self, length):
        if length == 1:
            print('-')
        else:


