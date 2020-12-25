from corners import Corner


class Camp:
    """
    Class representing a camp
    """

    NUM_OF_PAWNS = 19
    CAMP_WIDTH = 5
    BOX_WIDTH = 16

    def __init__(self, corner: 'Corner'):
        self._corner = corner
        self._cords = self._calculate_cords()

    def _calculate_cords(self):
        width = Camp.CAMP_WIDTH
        cords = []

        for y in range(Camp.CAMP_WIDTH):
            for x in range(width):
                if self.get_corner() == Corner.TOP_LEFT:
                    position = x, y
                elif self.get_corner() == Corner.TOP_RIGHT:
                    position = Camp.BOX_WIDTH - 1 - x, y
                elif self.get_corner() == Corner.BOTTOM_RIGHT:
                    position = Camp.BOX_WIDTH - 1 - x, Camp.BOX_WIDTH - 1 - y
                elif self.get_corner() == Corner.BOTTOM_LEFT:
                    position = x, Camp.BOX_WIDTH - 1 - y
                cords.append(position)
            if y != 0:
                width -= 1

        return cords

    def get_corner(self):
        return self._corner

    def get_cords(self):
        return self._cords
