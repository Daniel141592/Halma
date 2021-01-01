from board import Board
from player import Player
from corners import corners_list
from constants import NUM_OF_PLAYERS, COLORS
from exceptions import IncorrectIndexException, IncorrectMoveException

import random


class GameEngine():
    """
    Class representing a game
    """
    def __init__(self, players_names):
        self._players = self._initialize_players(players_names)
        self._board = Board(self._players)
        self._now_turn = random.choice(self._players)
        self._winner = None

    def make_move(self, old_position, new_position):
        try:
            if self.is_cascade_jumps():
                self._board.check_cascade_jump(old_position, new_position)
            self._board.make_move(self._now_turn, old_position, new_position)
            if not self.is_cascade_jumps():
                self._next_turn()
            self._winner = self._board.check_winner(self._players)
        except IncorrectIndexException as e:
            raise IncorrectMoveException(e.message)

    def _next_turn(self):
        now_turn_index = self._players.index(self._now_turn)
        if now_turn_index == len(self._players) - 1:
            self._now_turn = self._players[0]
        else:
            self._now_turn = self._players[now_turn_index + 1]

    def get_board(self):
        return self._board.get_squares()

    def get_players(self):
        return self._players

    def get_now_turn(self):
        return self._now_turn

    def is_cascade_jumps(self):
        return self._board.get_cascade_jumps_position() is not None

    def end_cascade_jumps(self):
        self._board.set_cascade_jumps_position(None)
        self._next_turn()

    def get_winner(self):
        return self._winner

    def _initialize_players(self, players_names):
        players = []
        for color, corner, name in zip(
              self._colors_shuffle(), self._prepare_corners(), players_names):
            players.append(Player(color, corner, name))
        return players

    def _colors_shuffle(self):
        random_shuffle = random.sample(COLORS, len(COLORS))
        return random_shuffle[0:NUM_OF_PLAYERS]

    def _prepare_corners(self):
        return corners_list[0:NUM_OF_PLAYERS]
