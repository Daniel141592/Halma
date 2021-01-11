from player import Player
from corners import Corner


def test_creating_player():
    color = "white"
    corner = Corner.TOP_LEFT
    name = "Player 1"
    player = Player(name, color, corner)

    assert player.get_name() == name
    assert player.get_color() == color
    assert player.get_camp().get_corner() == corner
    assert player.get_opposite_camp().get_corner() == Corner.BOTTOM_RIGHT


def test_creating_empty_player():
    player = Player()
    assert player.get_name() == "NoName"
    assert player.get_color() is None
    assert player.get_camp() is None
    assert player.get_opposite_camp() is None


def test_initialize_player():
    color = "white"
    corner = Corner.TOP_LEFT
    name = "Player 1"
    player = Player(name)
    player.initialize_player(color, corner)

    assert player.get_name() == name
    assert player.get_color() == color
    assert player.get_camp().get_corner() == corner
    assert player.get_opposite_camp().get_corner() == Corner.BOTTOM_RIGHT
