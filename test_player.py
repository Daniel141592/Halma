from player import Player
from corners import Corner


def test_creating_player():
    color = "white"
    corner = Corner.TOP_LEFT
    name = "Player 1"
    player = Player(color, corner, name)

    assert player.get_name() == name
    assert player.get_color() == color
    assert player.get_camp().get_corner() == corner
