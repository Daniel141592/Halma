from constants import BOARD_WIDTH
from pawn import Pawn
from player import Player
from incorrect_move_exception import IncorrectMoveException


class Board():
    """
    Class representing a board on which the game is playing
    """
    def __init__(self, players):
        self._squares = [[Pawn()] * BOARD_WIDTH for _ in range(BOARD_WIDTH)]
        self._arrange_pawns(players)

    def _get_square(self, position):
        x, y = position
        return self._squares[y][x]

    def _set_square(self, position, pawn):
        x, y = position
        self._squares[y][x] = pawn

    def get_squares(self):
        return self._squares

    def _arrange_pawns(self, players):
        for player in players:
            for position in player.get_camp().get_coords():
                self._set_square(position, Pawn(player))

    def make_move(self, now_turn: 'Player', old_position, new_position):
        if old_position == new_position:
            raise IncorrectMoveException("That move makes no sense")
        if self._get_square(old_position).get_owner() != now_turn:
            raise IncorrectMoveException(
                    "Player doesn't have a pawn at this position")
        if not self._get_square(new_position).is_empty():
            raise IncorrectMoveException("This square is not free")

        x_diff = abs(old_position[0] - new_position[0])
        y_diff = abs(old_position[1] - new_position[1])

        if x_diff > 1 or y_diff > 1:
            raise IncorrectMoveException("You cannot move so far")

        self._move_pawn(old_position, new_position)

    def _move_pawn(self, old_position, new_position):
        self._set_square(new_position, self._get_square(old_position))
        self._set_square(old_position, Pawn())

    def check_winner(self):
        pass
