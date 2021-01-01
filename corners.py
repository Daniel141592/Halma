from enum import Enum


class Corner(Enum):
    TOP_LEFT = 1
    TOP_RIGHT = 2
    BOTTOM_RIGHT = 3
    BOTTOM_LEFT = 4


corners_list = [
    Corner.TOP_LEFT, Corner.BOTTOM_RIGHT, Corner.TOP_RIGHT, Corner.BOTTOM_LEFT
]

opposite_corner = {
    Corner.TOP_LEFT: Corner.BOTTOM_RIGHT,
    Corner.TOP_RIGHT: Corner.BOTTOM_LEFT,
    Corner.BOTTOM_RIGHT: Corner.TOP_LEFT,
    Corner.BOTTOM_LEFT: Corner.TOP_RIGHT
}
