from game_engine import GameEngine
from exceptions import IncorrectMoveException
from player import Player
from bot import Bot


def main():
    game_mode = choose_game_mode()

    if game_mode == 1:
        num_of_physical_players = 2
        num_of_bots = 0
    elif game_mode == 2:
        num_of_physical_players = 1
        num_of_bots = 1
    elif game_mode == 3:
        num_of_physical_players = 0
        num_of_bots = 2

    players = []
    for _ in range(num_of_physical_players):
        print("Podaj nazwę gracza:")
        name = input()
        players.append(Player(name.strip()))

    bots = {}
    for i in range(num_of_bots):
        player = Player(f"{i + 1} Bot")
        players.append(player)
        bots[player] = Bot(player)

    game = GameEngine(players)

    while game.get_winner() is None:
        display_board(game.get_board())
        now_turn = game.get_now_turn()

        print(f"Kolej gracza {now_turn.get_name()}")
        if now_turn not in bots and game.is_cascade_jumps():
            print("Wpisz 'k', aby zakończyć sekwencję ruchów")
        try:
            if now_turn in bots:
                user_input = bots[now_turn].make_move(game.get_board(),
                                                      game.is_cascade_jumps())
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

    display_board(game.get_board())
    print(f"Wygrał gracz {game.get_winner().get_name()}")


def parse_input(move):
    old_x = int(move[0:move.index(',')].strip())
    old_y = int(move[move.index(',')+1:move.index('->')].strip())

    new_x = int(move[move.index('->')+2:move.rindex(',')].strip())
    new_y = int(move[move.rindex(',')+1:])

    return ((old_x, old_y), (new_x, new_y))


def display_board(board):
    for row in board:
        row_str = ""
        for sign in row:
            row_str += f"{sign} "
        print(row_str)


def choose_game_mode():
    print("Wybierz tryb gry: ")
    print("1. Dwóch graczy")
    print("2. Gracz vs komputer")
    print("3. Komputer vs komputer")
    return int(input())


if __name__ == "__main__":
    main()
