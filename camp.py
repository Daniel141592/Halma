from corners import Corner
from constants import CAMP_WIDTH, BOARD_WIDTH


class Camp:
    """
    Class representing a camp
    """
    def __init__(self, corner: 'Corner'):
        self._corner = corner
        self._coords = self._calculate_coords()

    def _calculate_coords(self):
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

    def get_corner(self):
        return self._corner

    def get_coords(self):
        return self._coords
