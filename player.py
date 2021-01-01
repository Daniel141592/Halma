from corners import Corner, opposite_corner
from camp import Camp


class Player:
    """
    Class representing a Player
    """
    def __init__(self, color, corner: Corner, name=None):
        self._color = color
        self._camp = Camp(corner)
        self._opposite_camp = Camp(opposite_corner[corner])
        self._name = name if name is not None else "NoName"

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_camp(self):
        return self._camp

    def get_opposite_camp(self):
        return self._opposite_camp
