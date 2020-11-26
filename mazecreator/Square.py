import pygame

import mazecreator.settings as settings
from mazecreator.SquareState import SquareState


class Square:
    def __init__(self, row, col):
        self.width = settings.SQUARE_WIDTH
        self.x = row * self.width
        self.y = col * self.width
        self.row = row
        self.col = col
        if self.row in [0, settings.ROWS - 1] or self.col in [0, settings.ROWS - 1]:
            self.state = SquareState.WALL
        else:
            self.state = SquareState.EMPTY
        self.neighbours = []

    def __repr__(self):
        return f'Square (x, y): ({self.x},{self.y}) in (row, col) ({self.row},{self.col}) of {self.state}'

    def reset(self):
        self.state = SquareState.EMPTY

    def is_visited(self):
        return self.state == SquareState.VISITED

    def is_wall(self):
        return self.state == SquareState.WALL

    def is_start(self):
        return self.state == SquareState.START

    def is_end(self):
        return self.state == SquareState.END

    def is_open(self):
        return self.state == SquareState.OPEN

    def change_state(self, state: SquareState):
        self.state = state

    def _get_colour_from_state(self):
        """
        Get the colour square should be depending on its state
        :return: colour RGB as a triple (3-tuple, tuple with 3 values)
        :rtype: tuple
        """

        if self.state == SquareState.EMPTY:
            return settings.EMPTY_COLOUR
        elif self.state == SquareState.START:
            return settings.START_COLOUR
        elif self.state == SquareState.END:
            return settings.END_COLOUR
        elif self.state == SquareState.WALL:
            return settings.WALL_COLOUR
        elif self.state == SquareState.VISITED:
            return settings.VISITED_COLOUR
        elif self.state == SquareState.OPEN:
            return settings.OPEN_COLOUR
        elif self.state == SquareState.PATH:
            return settings.PATH_COLOUR

    def get_pos(self):
        """
        Return position of a square
        :return: position
        :rtype : tuple
        """

        return self.row, self.col

    def draw(self, win):
        pygame.draw.rect(win, self._get_colour_from_state(), (self.x, self.y, self.width, self.width))
