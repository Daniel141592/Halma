from board import Board
from player import Player
from pawn import Pawn
from corners import Corner
from constants import BOARD_WIDTH
from incorrect_move_exception import IncorrectMoveException

import pytest


def test_creating_board_and_arrange_pawns():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    players = [player_1, player_2]
    board = Board(players)

    assert len(board.get_squares()) == BOARD_WIDTH
    assert all(len(row) == BOARD_WIDTH for row in board.get_squares())

    for player in players:
        coords = player.get_camp().get_coords()
        for position in coords:
            x, y = position
            assert not board.get_squares()[y][x].is_empty()
            assert board.get_squares()[y][x].get_owner() == player

    assert board.get_squares()[3][3].is_empty()


def test__get_square():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    x = 2
    y = 3
    board = Board([player_1, player_2])
    assert board._get_square((x, y)) == board.get_squares()[y][x]


def test__get_square_negative_index():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._get_square((-2, 3))


def test__get_square_incorrect_index():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._get_square((22, 3))


def test__get_square_wrong_type_of_index():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._get_square((2.6, 3))


def test__get_square_wrong_type_of_index_2():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._get_square(("abc", 3))


def test__set_square():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    position = 2, 3
    pawn = Pawn(player_1)
    board = Board([player_1, player_2])
    board._set_square(position, pawn)
    assert board._get_square(position) == pawn


def test__set_square_negative_index():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    position = -2, 3
    pawn = Pawn(player_1)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._set_square(position, pawn)


def test__set_square_incorrect_index():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    position = 2, 33
    pawn = Pawn(player_1)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._set_square(position, pawn)


def test__set_square_wrong_type_of_index():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    position = 2, 3.5
    pawn = Pawn(player_1)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._set_square(position, pawn)


def test__set_square_wrong_type_of_index_2():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    position = 2, "abc"
    pawn = Pawn(player_1)
    board = Board([player_1, player_2])
    with pytest.raises(IncorrectMoveException):
        board._set_square(position, pawn)


def test__move_pawn():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    old_position = (4, 0)
    new_position = (5, 0)
    board._move_pawn(old_position, new_position)
    assert board._get_square(new_position).get_owner() == player_1


def test_make_move_correct_move():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    old_position = (4, 0)
    new_position = (5, 1)
    board.make_move(player_1, old_position, new_position)
    assert board._get_square(old_position).is_empty()
    assert board._get_square(new_position).get_owner() == player_1


def test_make_move_to_the_same_position():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    position = (4, 0)
    with pytest.raises(IncorrectMoveException):
        board.make_move(player_1, position, position)


def test_make_move_from_wrong_position():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    old_position = (14, 0)
    new_position = (5, 1)
    with pytest.raises(IncorrectMoveException):
        board.make_move(player_1, old_position, new_position)


def test_make_move_to_already_taken_position():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    old_position = (0, 0)
    new_position = (0, 1)
    with pytest.raises(IncorrectMoveException):
        board.make_move(player_1, old_position, new_position)


def test_make_move_incorrect_move():
    player_1 = Player("white", Corner.TOP_LEFT)
    player_2 = Player("black", Corner.BOTTOM_RIGHT)
    board = Board([player_1, player_2])
    old_position = (4, 0)
    new_position = (8, 1)
    with pytest.raises(IncorrectMoveException):
        board.make_move(player_1, old_position, new_position)
