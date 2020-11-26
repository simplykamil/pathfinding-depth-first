import pygame

import mazecreator.picasso as picasso
import mazecreator.settings as settings
from mazecreator.SquareState import SquareState


class Creator:
    @staticmethod
    def get_grid():
        WINDOW = pygame.display.set_mode((settings.WIDTH, settings.WIDTH))
        GRID = picasso.make_grid(settings.ROWS, settings.WIDTH)
        pygame.display.set_caption(settings.WINDOW_TITLE)

        start_pos = None
        end_pos = None

        run = True
        while run:
            picasso.draw(WINDOW, GRID)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    run = False
                elif pygame.mouse.get_pressed()[0]:
                    row, col = picasso.get_clicked_pos(pygame.mouse.get_pos())
                    square = GRID[row][col]

                    if not start_pos and square != end_pos and square.state != SquareState.WALL:
                        start_pos = square
                        start_pos.change_state(SquareState.START)
                    elif not end_pos and square != start_pos and square.state != SquareState.WALL:
                        end_pos = square
                        end_pos.change_state(SquareState.END)
                    elif square not in (start_pos, end_pos):
                        square.change_state(SquareState.WALL)

                elif pygame.mouse.get_pressed()[2]:
                    row, col = picasso.get_clicked_pos(pygame.mouse.get_pos())
                    square = GRID[row][col]
                    square.reset()

                    if square == start_pos:
                        start_pos = None
                    elif square == end_pos:
                        end_pos = None

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if start_pos and end_pos:
                            return GRID

        pygame.quit()


if __name__ == '__main__':
    GRID = Creator.get_grid()

    print()
    [print(x) for x in GRID]
