import pygame

import mazecreator.rgbcolours as colours
import mazecreator.settings as settings
from mazecreator.Square import Square


def make_grid(rows: int, width: int):
    """
    Create grid
    :param rows: number of rows
    :param width: width
    :return: grid
    :rtype: list
    """

    grid = list()
    for row in range(rows):
        grid.append(list())
        for col in range(rows):
            grid[row].append(Square(row, col))

    return grid


def draw_grid(win, rows, width):
    for i in range(rows):
        pygame.draw.line(win, settings.LINE_COLOUR, (0, i * settings.GAP), (width, i * settings.GAP))
        for j in range(rows):
            pygame.draw.line(win, settings.LINE_COLOUR, (j * settings.GAP, 0), (j * settings.GAP, width))


def draw(win, grid, rows=settings.ROWS, width=settings.WIDTH):
    win.fill(colours.WHITE)

    for row in grid:
        for square in row:
            square.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos):
    y, x = pos

    row = y // settings.GAP
    col = x // settings.GAP

    return row, col
