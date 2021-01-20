from player import Player


class Pawn():
    """
    Class representing a pawn

    Attributes

    owner: Player
        Player owning the Pawn

    is_transferred_to_opponent_camp: bool
        Set to true when the Pawn is in opponent camp

    is_empty: bool
        'empty Pawn' means there is free square at this position
        Free squares on board are represented by Pawn object with
        is_empty set to true and owner set to false
    """
    def __init__(self, owner: 'Player' = None):
        self._owner = owner
        self._transferred_to_opponent_camp = False
        self._is_empty = owner is None

    def __str__(self):
        return ' ' if self._is_empty else '●'

    def __repr__(self):
        return self.__str__()

    def get_owner(self):
        return self._owner

    def is_empty(self):
        return self._is_empty

    def get_color(self):
        return self._owner.get_color()

    def is_transferred_to_opponent_camp(self):
        return self._transferred_to_opponent_camp

    def set_transferred_to_opponent_camp(self, transferred=None):
        if transferred is None:
            self._transferred_to_opponent_camp = True
        else:
            self._transferred_to_opponent_camp = transferred
