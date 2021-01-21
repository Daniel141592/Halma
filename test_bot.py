from bot import Bot
from player import Player
from pawn import Pawn
from constants import BOARD_WIDTH
from corners import Corner
from color import Color
from game_engine import GameEngine


def test_creating_bot():
    player = Player()
    bot = Bot(player)
    assert bot._player == player
    assert bot._last_move is None


def test_make_move(monkeypatch):
    def mock_choice(a):
        return (0, 4), (1, 5)

    monkeypatch.setattr("bot.choice", mock_choice)

    players = [Player("player1"), Player("player2")]
    bot = Bot(players[0])
    game = GameEngine(players)
    board = game.get_board()
    # every coordinate should be more by one
    assert bot.make_move(board, None) == '1,5->2,6'


def test_make_move_2(monkeypatch):
    def mock_is_move_reasonable(a, b, c):
        return False
    monkeypatch.setattr("bot.Bot._is_move_reasonable", mock_is_move_reasonable)
    players = [Player("player1"), Player("player2")]
    bot = Bot(players[0])
    game = GameEngine(players)
    board = game.get_board()
    assert bot.make_move(board, None) == 'k'


def test_prepare_owned_pawns_positions():
    player = Player("name")
    bot = Bot(player)
    board = [[Pawn()] * BOARD_WIDTH for _ in range(BOARD_WIDTH)]
    board[0][0] = board[0][1] = Pawn(player)
    positions = bot._prepare_owned_pawns_positions(board)
    expected = [
        (0, 0),
        (1, 0)
    ]
    assert positions == expected


def test_check_possible_standard_moves():
    players = [Player("player1"), Player("player2")]
    bot = Bot(players[0])
    game = GameEngine(players)
    board = game.get_board()
    position = 4, 0
    expected = [(5, 0), (5, 1)]
    assert bot._check_possible_standard_moves(board, position) == expected


def test_check_possible_standard_moves_2():
    players = [Player("player1"), Player("player2")]
    bot = Bot(players[1])
    game = GameEngine(players)
    board = game.get_board()
    position = 12, 13
    expected = [(11, 12), (11, 13), (12, 12)]
    assert bot._check_possible_standard_moves(board, position) == expected


def test_check_possible_jumps():
    players = [Player("player1"), Player("player2")]
    bot = Bot(players[0])
    game = GameEngine(players)
    board = game.get_board()
    position = 1, 1
    expected = [(3, 3)]
    assert bot._check_possible_jumps(board, position) == expected


def test_check_possible_jumps_2():
    players = [Player("player1"), Player("player2")]
    bot = Bot(players[1])
    game = GameEngine(players)
    board = game.get_board()
    position = 14, 14
    expected = [(12, 12)]
    assert bot._check_possible_jumps(board, position) == expected


def test_is_move_reasonable():
    player = Player("player1", Color.WHITE, Corner.TOP_LEFT)
    bot = Bot(player)
    old_pos = 0, 0
    new_pos = 13, 13
    move = old_pos, new_pos
    assert bot._is_move_reasonable(move, False)


def test_is_move_reasonable_2():
    player = Player("player1", Color.WHITE, Corner.TOP_LEFT)
    bot = Bot(player)
    old_pos = 14, 14
    new_pos = 12, 12
    move = old_pos, new_pos
    assert not bot._is_move_reasonable(move, True)


def test_is_move_reasonable_3():
    player = Player("player1", Color.WHITE, Corner.TOP_LEFT)
    bot = Bot(player)
    old_pos = 1, 1
    new_pos = 3, 3
    move = old_pos, new_pos
    assert bot._is_move_reasonable(move, True)


def test_is_move_reasonable_4():
    player = Player("player1", Color.WHITE, Corner.TOP_LEFT)
    bot = Bot(player)
    old_pos = 6, 6
    new_pos = 5, 6
    move = old_pos, new_pos
    assert not bot._is_move_reasonable(move, True)


def test_calculate_distance():
    a = 0, 0
    b = 3, 4
    bot = Bot(Player("name"))
    assert bot._calculate_distance(a, b) == 5


def test_get_pawn_between():
    board = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    bot = Bot(Player("name"))
    a = 2, 2
    b = 2, 0
    assert bot._get_pawn_between(board, a, b) == 6


def test_format_move_text():
    bot = Bot(Player("name"))
    move = (0, 1), (1, 2)
    assert bot._format_move_text(move) == "1,2->2,3"
