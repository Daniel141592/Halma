from pawn import Pawn
from player import Player
from color import Color
from corners import Corner
from escape_codes import ANSI_ESCAPE_CODES as AEC
import text_interface


def test_parse_input():
    move = "1,1->2,2"
    expected = (0, 0), (1, 1)
    assert text_interface.parse_input(move) == expected


def test_parse_input_2():
    move = " 1, 1 -> 2, 1"
    expected = (0, 0), (1, 0)
    assert text_interface.parse_input(move) == expected


def test_players_division():
    game_mode = 1
    physycal, bots = text_interface.get_players_division(game_mode)
    assert physycal == 2
    assert bots == 0


def test_players_division_2():
    game_mode = 2
    physycal, bots = text_interface.get_players_division(game_mode)
    assert physycal == 1
    assert bots == 1


def test_players_division_3():
    game_mode = 3
    physycal, bots = text_interface.get_players_division(game_mode)
    assert physycal == 0
    assert bots == 2


def test_create_bots():
    bots = text_interface.create_bots(2)
    for i, bot in enumerate(bots):
        assert bot.get_name() == f"Bot {i+1}"
        assert bots[bot]._player == bot


def test_choose_color():
    pawn1 = Pawn(Player("name", Color.WHITE))
    pawn2 = Pawn(Player("name", Color.BLACK))
    assert text_interface.choose_color(pawn1) == AEC.YELLOW
    assert text_interface.choose_color(pawn2) == AEC.BLUE


def test_choose_bg_color():
    assert text_interface.choose_bg_color((0, 1), [(3, 0)]) == AEC.BG_BLACK
    assert text_interface.choose_bg_color((1, 1), [(3, 0)]) == AEC.BG_WHITE
    assert text_interface.choose_bg_color((0, 1), [(0, 1)]) == AEC.BG_MAGENTA


def test_get_camps_coords():
    players = [
        Player("first_player", Color.WHITE, Corner.TOP_LEFT),
        Player("second_player", Color.BLACK, Corner.BOTTOM_RIGHT)
    ]
    camp_coords = text_interface.get_camps_coords(players)
    first_player_coords = players[0].get_camp().get_coords()
    second_player_coords = players[1].get_camp().get_coords()
    assert all(pos in camp_coords for pos in first_player_coords)
    assert all(pos in camp_coords for pos in second_player_coords)
