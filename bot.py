from player import Player
from constants import BOARD_WIDTH, DELAY
from itertools import product

from random import choice
from math import hypot
from time import sleep


class Bot:
    """
    Class representing a bot

    Attributes

    player: Player
        Player object controlled by the bot

    last_move: tuple
        Contains positions of last move done by bot
    """
    def __init__(self, player: 'Player'):
        self._player = player
        self._last_move = None

    def make_move(self, board, cascade_jumps_position):
        sleep(DELAY)
        is_cascade_jump = cascade_jumps_position is not None

        owned_pawns_positions = self._prepare_owned_pawns_positions(board)
        potential_moves = []
        for old_pos in owned_pawns_positions:
            if is_cascade_jump and old_pos != cascade_jumps_position:
                continue
            for pos in self._check_possible_jumps(board, old_pos):
                move = old_pos, pos
                if self._is_move_reasonable(move, is_cascade_jump):
                    potential_moves.append(move)
            if not is_cascade_jump:
                for pos in self._check_possible_standard_moves(board, old_pos):
                    move = old_pos, pos
                    if self._is_move_reasonable(move, is_cascade_jump):
                        potential_moves.append(move)
        if len(potential_moves) == 0:
            return 'k'
        self._last_move = choice(potential_moves)
        return self._format_move_text(self._last_move)

    def _prepare_owned_pawns_positions(self, board):
        owned_pawns = []
        for row_index, row in enumerate(board):
            for column_index, pawn in enumerate(row):
                if not pawn.is_empty() and pawn.get_owner() == self._player:
                    owned_pawns.append((column_index, row_index))
        return owned_pawns

    def _check_possible_standard_moves(self, board, position):
        return self._check_possible_moves(board, position, False)

    def _check_possible_jumps(self, board, position):
        return self._check_possible_moves(board, position, True)

    def _check_possible_moves(self, board, position, checking_jumps):
        unit = 2 if checking_jumps else 1
        current_x, current_y = position
        potential_positions = []
        for x, y in product((-unit, 0, unit), (-unit, 0, unit)):
            if x == y and y == 0:
                continue
            if current_x + x not in range(BOARD_WIDTH) or \
                    current_y + y not in range(BOARD_WIDTH):
                continue
            new_pos = current_x + x, current_y + y
            if self._get_pawn_between(board, position, new_pos).is_empty() \
                    and checking_jumps:
                continue
            if (new_pos, position) == self._last_move:
                continue
            if board[current_y + y][current_x + x].is_empty():
                potential_positions.append(new_pos)

        return potential_positions

    def _is_move_reasonable(self, move, is_cascade_jump):
        old_pos, new_pos = move
        target_camp = self._player.get_opposite_camp()
        target_position = target_camp.get_extreme_corner_postion()
        if new_pos in self._player.get_opposite_camp().get_coords() \
                and not is_cascade_jump:    # to prevent cyclic moves
            return True
        if self._calculate_distance(new_pos, target_position) <= \
                self._calculate_distance(old_pos, target_position):
            return True

        return False

    def _calculate_distance(self, position_a, position_b):
        a_x, a_y = position_a
        b_x, b_y = position_b
        return hypot(a_x - b_x, a_y - b_y)

    def _get_pawn_between(self, board, a, b):
        x = int((a[0] + b[0]) / 2)
        y = int((a[1] + b[1]) / 2)
        return board[y][x]

    def _format_move_text(self, move):
        old_position, new_position = move
        old_x, old_y = old_position
        new_x, new_y = new_position
        # +1 because interface subtracts 1
        return f"{old_x + 1},{old_y + 1}->{new_x + 1},{new_y + 1}"
