from camp import Camp
from corners import Corner


def test_creating_camp():
    corner = Corner.TOP_LEFT
    camp = Camp(corner)
    assert camp.get_corner() == corner


def test_calculating_coords_top_left():
    corner = Corner.TOP_LEFT
    camp = Camp(corner)
    expected_coords = [
        (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
        (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
        (0, 2), (1, 2), (2, 2), (3, 2),
        (0, 3), (1, 3), (2, 3),
        (0, 4), (1, 4)
    ]
    assert len(camp.get_coords()) == 19
    assert camp.get_coords() == expected_coords


def test_calculating_coords_top_right():
    corner = Corner.TOP_RIGHT
    camp = Camp(corner)
    expected_coords = [
        (15, 0), (14, 0), (13, 0), (12, 0), (11, 0),
        (15, 1), (14, 1), (13, 1), (12, 1), (11, 1),
        (15, 2), (14, 2), (13, 2), (12, 2),
        (15, 3), (14, 3), (13, 3),
        (15, 4), (14, 4)
    ]
    assert len(camp.get_coords()) == 19
    assert camp.get_coords() == expected_coords


def test_calculating_coords_bottom_right():
    corner = Corner.BOTTOM_RIGHT
    camp = Camp(corner)
    expected_coords = [
        (15, 15), (14, 15), (13, 15), (12, 15), (11, 15),
        (15, 14), (14, 14), (13, 14), (12, 14), (11, 14),
        (15, 13), (14, 13), (13, 13), (12, 13),
        (15, 12), (14, 12), (13, 12),
        (15, 11), (14, 11)
    ]
    assert len(camp.get_coords()) == 19
    assert camp.get_coords() == expected_coords


def test_calculating_coords_bottom_left():
    corner = Corner.BOTTOM_LEFT
    camp = Camp(corner)
    expected_coords = [
        (0, 15), (1, 15), (2, 15), (3, 15), (4, 15),
        (0, 14), (1, 14), (2, 14), (3, 14), (4, 14),
        (0, 13), (1, 13), (2, 13), (3, 13),
        (0, 12), (1, 12), (2, 12),
        (0, 11), (1, 11)
    ]
    assert len(camp.get_coords()) == 19
    assert camp.get_coords() == expected_coords
