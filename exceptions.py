class IncorrectMoveException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message


class IncorrectIndexException(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message
