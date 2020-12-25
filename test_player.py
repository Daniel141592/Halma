from player import Player
from corners import Corner
from camp import Camp
from incorrect_move_exception import IncorrectMoveException

import pytest


def test_creating_player():
    color = "white"
    corner = Corner.TOP_LEFT
    name = "Player 1"
    player = Player(color, corner, name)

    assert player.get_name() == name
    assert player.get_color() == color
    assert player.get_camp().get_corner() == corner


def test_arrange_pawns():
    corner = Corner.TOP_LEFT
    camp = Camp(corner)
    col = "white"
    player = Player(col, corner)
    cords = [pawn.get_position() for pawn in player._arrange_pawns(col, camp)]
    expected_cords = camp.get_cords()
    assert cords == expected_cords


def test_move_pawn():
    player = Player("white", Corner.BOTTOM_LEFT)
    old_cords = (0, 11)
    new_cords = (1, 10)
    player.move_pawn(old_cords, new_cords)
    assert player.get_pawn_at_position(new_cords) is not None


def test_move_pawn_from_incorrect_position():
    player = Player("Black", Corner.BOTTOM_RIGHT)
    old_cords = (0, 11)
    new_cords = (1, 10)
    with pytest.raises(IncorrectMoveException):
        player.move_pawn(old_cords, new_cords)
