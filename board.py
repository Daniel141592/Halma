from constants import BOARD_WIDTH
from pawn import Pawn
from player import Player
from exceptions import IncorrectMoveException, IncorrectIndexException

from itertools import product


class Board():
    """
    Class representing a board on which the game is playing
    """
    def __init__(self, players):
        self._squares = [[Pawn()] * BOARD_WIDTH for _ in range(BOARD_WIDTH)]
        self._arrange_pawns(players)
        self._cascade_jumps_position = None

    def _get_square(self, position):
        try:
            x, y = position
            if x < 0 or y < 0:
                raise IncorrectIndexException("Value cannot be negative")
            return self._squares[y][x]
        except (TypeError, IndexError):
            raise IncorrectIndexException("Incorrect index of square")

    def _set_square(self, position, pawn):
        try:
            x, y = position
            if x < 0 or y < 0:
                raise IncorrectIndexException("Value cannot be negative")
            self._squares[y][x] = pawn
        except (TypeError, IndexError):
            raise IncorrectIndexException("Incorrect index of square")

    def get_squares(self):
        return self._squares

    def get_cascade_jumps_position(self):
        return self._cascade_jumps_position

    def set_cascade_jumps_position(self, position):
        self._cascade_jumps_position = position

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

        if self._is_jump(old_position, new_position) and \
                self._is_further_jump_possible(old_position, new_position):
            self.set_cascade_jumps_position(new_position)
        else:
            self.set_cascade_jumps_position(None)

        self._move_pawn(old_position, new_position)

    def _is_jump(self, old_position, new_position):
        x_diff = abs(old_position[0] - new_position[0])
        y_diff = abs(old_position[1] - new_position[1])

        if x_diff > 2 or y_diff > 2:
            raise IncorrectMoveException("You cannot move so far")
        if (x_diff in (0, 2)) and (y_diff in (0, 2)):
            if self._get_square_between(old_position, new_position).is_empty():
                raise IncorrectMoveException("There is nothing to jump over")
            else:
                return True
        elif x_diff > 1 or y_diff > 1:
            raise IncorrectMoveException("Incorrect jump")

        return False

    def _is_further_jump_possible(self, old_position, new_position):
        current_x, current_y = new_position
        for x, y in product((-2, 0, 2), (-2, 0, 2)):
            position = current_x + x, current_y + y
            if position == old_position or position == new_position:
                continue
            try:
                if self._get_square(position).is_empty() and not \
                  self._get_square_between(new_position, position).is_empty():
                    return True
            except IncorrectIndexException:
                continue
        return False

    def check_cascade_jump(self, old_position, new_position):
        if self.get_cascade_jumps_position() != old_position:
            raise IncorrectMoveException("Incorrect cascade jump")
        if not self._is_jump(old_position, new_position):
            raise IncorrectMoveException("This is not a jump")

    def _get_square_between(self, a, b):
        x = int((a[0] + b[0]) / 2)
        y = int((a[1] + b[1]) / 2)
        return self._get_square((x, y))

    def _move_pawn(self, old_position, new_position):
        self._set_square(new_position, self._get_square(old_position))
        self._set_square(old_position, Pawn())

    def check_winner(self, players):
        for player in players:
            is_winner = True
            for position in player.get_opposite_camp().get_coords():
                if self._get_square(position).get_owner() != player:
                    is_winner = False
                    break
            if is_winner:
                return player
        return None
