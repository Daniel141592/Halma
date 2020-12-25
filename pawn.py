class Pawn():
    """
    Class representing a pawn
    """
    def __init__(self, x, y, color):
        self.move(x, y)
        self._color = color
        self._transferred_to_opponent_camp = False

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    def get_position(self):
        return self.get_x(), self.get_y()

    def get_color(self):
        return self._color

    def is_transferred_to_opponent_camp(self):
        return self._transferred_to_opponent_camp

    def set_transferred_to_opponent_camp(self, transferred=None):
        if transferred is None:
            self._transferred_to_opponent_camp = True
        else:
            self._transferred_to_opponent_camp = transferred

    def move(self, x, y):
        self._x = x
        self._y = y
