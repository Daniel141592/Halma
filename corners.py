from enum import Enum
from constants import BOARD_WIDTH


class Corner(Enum):
    TOP_LEFT = 1
    BOTTOM_RIGHT = 2
    TOP_RIGHT = 3
    BOTTOM_LEFT = 4

    def get_opposite_corner(self):
        opposite_corners = {
            1: Corner.BOTTOM_RIGHT,
            2: Corner.TOP_LEFT,
            3: Corner.BOTTOM_LEFT,
            4: Corner.TOP_RIGHT
        }
        return opposite_corners[self.value]

    def get_extreme_corner_postion(self):
        extreme_corners_positions = {
            1: (0, 0),
            2: (BOARD_WIDTH - 1, BOARD_WIDTH - 1),
            3: (BOARD_WIDTH - 1, 0),
            4: (0, BOARD_WIDTH - 1)
        }
        return extreme_corners_positions[self.value]
