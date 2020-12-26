from game_engine import GameEngine


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
