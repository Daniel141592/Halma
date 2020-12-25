from pawn import Pawn
from corners import Corner
from camp import Camp
from incorrect_move_exception import IncorrectMoveException


class Player:
    """
    Class representing a Player
    """
    def __init__(self, color, corner: Corner, name=None):
        self._color = color
        self._camp = Camp(corner)
        self._name = name
        self._pawns = self._arrange_pawns(color, self.get_camp())

    def _arrange_pawns(self, color, camp):
        pawns = []
        for position in camp.get_cords():
            x, y = position
            pawns.append(Pawn(x, y, color))
        return pawns

    def get_name(self):
        return self._name

    def get_color(self):
        return self._color

    def get_camp(self):
        return self._camp

    def get_pawns(self):
        return self._pawns

    def get_pawn_at_position(self, position):
        for pawn in self.get_pawns():
            if pawn.get_position() == position:
                return pawn
        return None

    def move_pawn(self, old_cords, new_cords):
        pawn_to_move = self.get_pawn_at_position(old_cords)
        if pawn_to_move is None:
            raise IncorrectMoveException(
                    "Player doesn't have a pawn at this position")
        x, y = new_cords
        pawn_to_move.move(x, y)
