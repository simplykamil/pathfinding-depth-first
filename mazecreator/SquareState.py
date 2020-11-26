import enum


class SquareState(enum.Enum):
    START = 0
    END = 1
    EMPTY = 2
    WALL = 3
    VISITED = 4
    OPEN = 5
    PATH = 6
