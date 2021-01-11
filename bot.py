from player import Player
from constants import BOARD_WIDTH
from itertools import product

from random import choice
from math import hypot


class Bot:
    def __init__(self, player: 'Player'):
        self._player = player

    def make_move(self, board, is_cascade_jumps):
        owned_pawns_positions = self._prepare_owned_pawns_positions(board)
        potential_moves = []
        for old_pos in owned_pawns_positions:
            for pos in self._check_possible_standard_moves(board, old_pos):
                potential_moves.append((old_pos, pos))
            # for pos in self._check_possible_jumps(board, old_pos):
            #     potential_moves.append((old_pos, pos))

        move = choice(potential_moves)
        while not self._is_move_reasonable(move):
            move = choice(potential_moves)
        return self._format_move_position(move)

    def _prepare_owned_pawns_positions(self, board):
        owned_pawns = []
        for row_index, row in enumerate(board):
            for column_index, pawn in enumerate(row):
                if not pawn.is_empty() and pawn.get_owner() == self._player:
                    owned_pawns.append((column_index, row_index))
        return owned_pawns

    def _check_possible_standard_moves(self, board, position):
        current_x, current_y = position
        potential_positions = []
        for x, y in product((-1, 0, 1), (-1, 0, 1)):
            if x == y and y == 0:
                continue
            if current_x + x not in range(BOARD_WIDTH) or \
                    current_y + y not in range(BOARD_WIDTH):
                continue
            if board[current_y + y][current_x + x].is_empty():
                potential_positions.append((current_x + x, current_y + y))

        return potential_positions

    def _check_possible_jumps(self, board, position):
        current_x, current_y = position
        potential_positions = []
        for x, y in product((-2, 0, 2), (-2, 0, 2)):
            if x == y and y == 0:
                continue
            if current_x + x not in range(BOARD_WIDTH) or \
                    current_y + y not in range(BOARD_WIDTH):
                continue
            new_pos = current_x + x, current_y + y
            if not self._get_pawn_between(board, position, new_pos).is_empty():
                potential_positions.append(new_pos)

        return potential_positions

    def _is_move_reasonable(self, move):
        old_position, new_position = move
        target_corner = self._player.get_opposite_camp().get_corner()
        target_position = target_corner.get_extreme_corner_postion()
        if new_position in self._player.get_opposite_camp().get_coords():
            return True
        if self._calculate_distance(new_position, target_position) <= \
                self._calculate_distance(old_position, target_position):
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

    def _format_move_position(self, position):
        old_position, new_position = position
        old_x, old_y = old_position
        new_x, new_y = new_position
        return f"{old_x},{old_y}->{new_x},{new_y}"
