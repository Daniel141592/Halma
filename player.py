from corners import Corner
from color import Color
from camp import Camp


class Player:
    """
    Class representing a Player

    Attributes

    name: string
        Name of the Player

    color: Color
        Enum object representing color of Player's pawns

    camp: Camp
        Object representing Player's camp

    opposite_camp: Camp
        Object representing camp of Player's opponent
    """
    def __init__(self, name=None, color: 'Color' = None, corner=None):
        self._name = name if name is not None else "NoName"
        self._color = color
        self._camp = None if corner is None else Camp(corner)
        if corner is not None:
            self._opposite_camp = self._camp.get_opposite_camp()
        else:
            self._opposite_camp = None

    def initialize_player(self, color: 'Color', corner: 'Corner'):
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
