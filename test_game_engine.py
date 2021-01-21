from game_engine import GameEngine
from corners import Corner
from color import Color
from player import Player


def test_creating_game_engine():
    players = [Player(), Player()]
    game = GameEngine(players)
    assert len(game._players) == len(players)
    assert game.get_now_turn() in game._players


def test_make_move(monkeypatch):
    def mock_choice(players):
        for player in players:
            if player.get_camp().get_corner() == Corner.TOP_LEFT:
                return player
    monkeypatch.setattr("game_engine.random.choice", mock_choice)

    players = [Player(), Player()]
    game = GameEngine(players)
    player = game.get_now_turn()
    old_position = (4, 0)
    new_position = (5, 0)
    x, y = new_position
    game.make_move(old_position, new_position)
    assert game.get_board()[y][x].get_owner() == player
    assert player is not game.get_now_turn()


def test__initialize_players():
    players = [Player("playerA"), Player("playerB")]

    game = GameEngine(players)
    players = game.get_players()
    assert players[0] == players[0]
    assert players[1] == players[1]
    assert all([player.get_color() in list(Color) for player in players])
    assert all([p.get_camp().get_corner() in list(Corner) for p in players])


def test__next_turn():
    game = GameEngine([Player(), Player()])
    player = game.get_now_turn()
    game._next_turn()
    assert player is not game.get_now_turn()


def test__colors_shuffle(monkeypatch):
    players = [Player("player1"), Player("player2")]
    game = GameEngine(players)

    def f(a, b):
        return list(Color)
    monkeypatch.setattr("game_engine.random.sample", f)
    assert len(game._colors_shuffle()) == len(players)
    assert game._colors_shuffle() == list(Color)


def test__prepare_corners():
    players = [Player("player1"), Player("player2")]
    game = GameEngine(players)

    assert len(game._prepare_corners()) == len(players)
