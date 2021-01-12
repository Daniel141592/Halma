from corners import Corner
from camp import Camp


class Player:
    """
    Class representing a Player
    """
    def __init__(self, name=None, color=None, corner=None):
        self._name = name if name is not None else "NoName"
        self._color = color
        self._camp = None if corner is None else Camp(corner)
        if corner is not None:
            self._opposite_camp = self._camp.get_opposite_camp()
        else:
            self._opposite_camp = None

    def initialize_player(self, color, corner: Corner):
        self._color = color
        self._camp = Camp(corner)
        self._opposite_camp = self._camp.get_opposite_camp()

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_camp(self):
        return self._camp

    def get_opposite_camp(self):
        return self._opposite_camp
