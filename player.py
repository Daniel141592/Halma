from corners import Corner
from camp import Camp


class Player:
    """
    Class representing a Player
    """
    def __init__(self, color, corner: Corner, name=None):
        self._color = color
        self._camp = Camp(corner)
        self._name = name if name is not None else "NoName"

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_camp(self):
        return self._camp
