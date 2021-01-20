from game_engine import GameEngine
from exceptions import IncorrectMoveException
from constants import BOARD_WIDTH
from player import Player
from bot import Bot
from escape_codes import ANSI_ESCAPE_CODES as AEC


def main():
    """
    Main function called when someone run the game
    """
    game_mode = None
    while not game_mode:
        game_mode = choose_game_mode()
    players_division = get_players_division(game_mode)
    num_of_physical_players, num_of_bots = players_division

    players = create_players(num_of_physical_players)
    bots = create_bots(num_of_bots, players)

    game = GameEngine(players)
    camps_coords = get_camps_coords(players)

    while game.get_winner() is None:
        make_move(game, bots, camps_coords)

    display_board(game.get_board(), camps_coords)
    text = f"Wygrał gracz {game.get_winner().get_name()}"
    colored_print(text, game.get_winner().get_color())


def make_move(game, bots, camps_coords):
    """
    Function getting input from player/bot and making a move
    Called in loop unless there is a winner
    """
    display_board(game.get_board(), camps_coords)
    now_turn = game.get_now_turn()

    text = f"Kolej gracza {now_turn.get_name()}"
    colored_print(text, now_turn.get_color())
    if now_turn not in bots and game.is_cascade_jumps():
        print("Wpisz 'k', aby zakończyć sekwencję ruchów")
    try:
        if now_turn in bots:
            user_input = bots[now_turn]. \
                make_move(game.get_board(),
                          game.get_cascade_jumps_position())
        else:
            user_input = input()
        if game.is_cascade_jumps() and user_input.strip() == 'k':
            game.end_cascade_jumps()
        else:
            old_position, new_position = parse_input(user_input)
            game.make_move(old_position, new_position)
    except ValueError:
        print("Incorrect input")
    except IncorrectMoveException as e:
        print(e.message)


def parse_input(move):
    old_x = int(move[0:move.index(',')].strip()) - 1
    old_y = int(move[move.index(',')+1:move.index('->')].strip()) - 1

    new_x = int(move[move.index('->')+2:move.rindex(',')].strip()) - 1
    new_y = int(move[move.rindex(',')+1:]) - 1

    return ((old_x, old_y), (new_x, new_y))


def display_board(board, camps_coords):
    print(horizontal_indices())
    for row_id, row in enumerate(board):
        row_str = ""
        for column_id, square in enumerate(row):
            color = choose_color(square)
            bg_color = choose_bg_color((column_id, row_id), camps_coords)
            row_str += f"{bg_color}{color}{square} {AEC.ENDC}"
        print(vertical_indices(row_id)+row_str)


def create_players(num_of_physical_players):
    players = []
    for _ in range(num_of_physical_players):
        print("Podaj nazwę gracza:")
        name = input()
        players.append(Player(name.strip()))
    return players


def get_players_division(game_mode):
    if game_mode == 1:
        num_of_physical_players = 2
        num_of_bots = 0
    elif game_mode == 2:
        num_of_physical_players = 1
        num_of_bots = 1
    elif game_mode == 3:
        num_of_physical_players = 0
        num_of_bots = 2
    else:
        return None
    return num_of_physical_players, num_of_bots


def create_bots(num_of_bots, players):
    bots = dict()
    for i in range(num_of_bots):
        player = Player(f"Bot {i + 1}")
        players.append(player)
        bots[player] = Bot(player)
    return bots


def colored_print(text, color):
    escape_code = AEC.YELLOW if color == "white" else AEC.BLUE
    print(escape_code+text+AEC.ENDC)


def choose_color(square):
    if not square.is_empty():
        # blue and yellow instead of black/white for better visibility
        if square.get_color() == 'black':
            color = AEC.BLUE
        elif square.get_color() == 'white':
            color = AEC.YELLOW
    else:
        color = AEC.WHITE
    return color


def choose_bg_color(position, special_positions=None):
    x, y = position
    if (x + y) % 2 == 0:
        if not special_positions or position in special_positions:
            bg_color = AEC.BG_CYAN
        else:
            bg_color = AEC.BG_WHITE
    else:
        if not special_positions or position in special_positions:
            bg_color = AEC.BG_MAGENTA
        else:
            bg_color = AEC.BG_BLACK
    return bg_color


def horizontal_indices():
    indices = '  '
    for i in range(BOARD_WIDTH):
        bg_color = choose_bg_color((1, i))
        indices += f"{bg_color}{(i + 1):2d}{AEC.ENDC}"
    return indices


def vertical_indices(row_id):
    bg_color = choose_bg_color((1, row_id))
    return bg_color+format(row_id+1, '2d')+AEC.ENDC


def get_camps_coords(players):
    camps_coords = []
    for player in players:
        for coords in player.get_camp().get_coords():
            camps_coords.append(coords)
    return camps_coords


def choose_game_mode():
    print("Wybierz tryb gry: ")
    print("1. Dwóch graczy")
    print("2. Gracz vs komputer")
    print("3. Komputer vs komputer")
    try:
        game_mode = int(input())
    except ValueError:
        return None
    return game_mode if game_mode in (1, 2, 3) else None


if __name__ == "__main__":
    main()
