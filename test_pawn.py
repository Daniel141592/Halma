from pawn import Pawn
from player import Player
from corners import Corner
from color import Color


def test_creating_pawn():
    color = Color.BLACK
    player = Player("name", color, Corner.TOP_LEFT)
    pawn = Pawn(player)
    assert pawn.get_owner() == player
    assert pawn.get_color() == color
    assert not pawn.is_empty()


def test_creating_empty_pawn():
    pawn = Pawn()
    assert pawn.is_empty()


def test_str_():
    player = Player("No name", Color.WHITE, Corner.BOTTOM_LEFT,)
    pawn = Pawn(player)
    assert str(pawn) == '●'


def test_repr():
    pawn = Pawn()
    assert repr(pawn) == ' '


def test_transferred_to_opponent_camp():
    color = Color.WHITE
    player = Player(color, Corner.TOP_LEFT)
    pawn = Pawn(player)

    pawn.set_transferred_to_opponent_camp(True)
    assert pawn.is_transferred_to_opponent_camp()

    pawn.set_transferred_to_opponent_camp(False)
    assert not pawn.is_transferred_to_opponent_camp()

    pawn.set_transferred_to_opponent_camp()
    assert pawn.is_transferred_to_opponent_camp()
