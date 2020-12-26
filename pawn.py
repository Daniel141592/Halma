from player import Player


class Pawn():
    """
    Class representing a pawn
    """
    def __init__(self, owner: 'Player' = None):
        self._owner = owner
        self._transferred_to_opponent_camp = False
        self._is_empty = owner is None

    def __str__(self):
        if self._is_empty:
            return '_'
        return self._owner.get_name()[0:1]

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
