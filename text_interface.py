from game_engine import GameEngine
from exceptions import IncorrectMoveException
from constants import NUM_OF_PLAYERS


def main():
    player_names = []
    for _ in range(NUM_OF_PLAYERS):
        print("Podaj nazwę gracza:")
        name = input()
        player_names.append(name.strip())

    game = GameEngine(player_names)

    while game.get_winner() is None:
        display_board(game.get_board())
        print(f"Kolej gracza {game.get_now_turn().get_name()}")
        if game.is_cascade_jumps():
            print("Wpisz 'k', aby zakończyć sekwencję ruchów")
        try:
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
    print(f"Wygrał gracz {game.get_winner()}")


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


if __name__ == "__main__":
    main()
