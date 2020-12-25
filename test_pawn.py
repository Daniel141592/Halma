from pawn import Pawn


def test_creating_pawn():
    x = 3
    y = 4
    color = "white"
    pawn = Pawn(x, y, color)
    assert pawn.get_x() == x
    assert pawn.get_y() == y
    assert pawn.get_position() == (x, y)
    assert pawn.get_color() == color


def test_move_pawn():
    pawn = Pawn(3, 4, "black")
    pawn.move(4, 5)
    assert pawn.get_position() == (4, 5)


def test_transferred_to_opponent_camp():
    pawn = Pawn(0, 0, "white")

    pawn.set_transferred_to_opponent_camp(True)
    assert pawn.is_transferred_to_opponent_camp()

    pawn.set_transferred_to_opponent_camp(False)
    assert not pawn.is_transferred_to_opponent_camp()

    pawn.set_transferred_to_opponent_camp()
    assert pawn.is_transferred_to_opponent_camp()
