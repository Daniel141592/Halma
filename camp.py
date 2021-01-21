from corners import Corner
from constants import CAMP_WIDTH, BOARD_WIDTH


class Camp:
    """
    Class representing a camp

    Attributes

    corner: Corner
        Enum object representing a corner

    extreme_corner: tuple
        Contains position of square in the corner of the camp
    """
    def __init__(self, corner: 'Corner'):
        self._corner = corner
        if corner == Corner.TOP_LEFT:
            self._extreme_corner = 0, 0
        elif corner == Corner.TOP_RIGHT:
            self._extreme_corner = BOARD_WIDTH - 1, 0
        elif corner == Corner.BOTTOM_RIGHT:
            self._extreme_corner = BOARD_WIDTH - 1, BOARD_WIDTH - 1
        elif corner == Corner.BOTTOM_LEFT:
            self._extreme_corner = 0, BOARD_WIDTH - 1

    def get_corner(self):
        return self._corner

    def get_extreme_corner_postion(self):
        return self._extreme_corner

    def get_coords(self):
        width = CAMP_WIDTH
        coords = []

        for y in range(CAMP_WIDTH):
            for x in range(width):
                if self.get_corner() == Corner.TOP_LEFT:
                    position = x, y
                elif self.get_corner() == Corner.TOP_RIGHT:
                    position = BOARD_WIDTH - 1 - x, y
                elif self.get_corner() == Corner.BOTTOM_RIGHT:
                    position = BOARD_WIDTH - 1 - x, BOARD_WIDTH - 1 - y
                elif self.get_corner() == Corner.BOTTOM_LEFT:
                    position = x, BOARD_WIDTH - 1 - y
                coords.append(position)
            if y != 0:
                width -= 1

        return coords

    def get_opposite_camp(self):
        if self.get_corner() == Corner.TOP_LEFT:
            return Camp(Corner.BOTTOM_RIGHT)
        if self.get_corner() == Corner.TOP_RIGHT:
            return Camp(Corner.BOTTOM_LEFT)
        if self.get_corner() == Corner.BOTTOM_RIGHT:
            return Camp(Corner.TOP_LEFT)
        elif self.get_corner() == Corner.BOTTOM_LEFT:
            return Camp(Corner.TOP_RIGHT)
