from game_engine import GameEngine
from constants import COLORS
from corners import corners_list


def test_creating_game_engine():
    players_names = ["player1", "player2"]
    game = GameEngine(players_names)
    assert len(game._players) == len(players_names)
    assert game.get_now_turn() in game._players


def test_make_move():
    players_names = ["player1", "player2"]
    game = GameEngine(players_names)
    player = game.get_now_turn()
    old_position = (4, 0)
    new_position = (5, 0)
    x, y = new_position
    game.make_move(old_position, new_position)
    assert game.get_board()[y][x].get_owner() == player
    assert player is not game.get_now_turn()


def test__initialize_players():
    players_names = ["playerA", "playerB"]
    game = GameEngine(players_names)
    players = game.get_players()
    assert len(players) == len(players_names)
    assert players[0].get_name() == players_names[0]
    assert players[1].get_name() == players_names[1]
    assert all([player.get_color() in COLORS for player in players])
    assert all([p.get_camp().get_corner() in corners_list for p in players])


def test__next_turn():
    game = GameEngine(["playerA", "playerB"])
    player = game.get_now_turn()
    game._next_turn()
    assert player is not game.get_now_turn()


def test__colors_shuffle(monkeypatch):
    players = ["player1", "player2"]
    game = GameEngine(players)

    def f(a, b):
        return COLORS
    monkeypatch.setattr("game_engine.random.sample", f)
    assert len(game._colors_shuffle()) == len(players)
    assert game._colors_shuffle() == COLORS


def test__prepare_corners():
    players = ["player1", "player2"]
    game = GameEngine(players)

    assert len(game._prepare_corners()) == len(players)
