import pygame
from pygame.locals import *

from programming_itmo.homework03.life import GameOfLife
from programming_itmo.homework03.ui import UI


class GUI(UI):

    def __init__(self, life: GameOfLife, cell_size: int=10, speed: int=10) -> None:
        super().__init__(life)

    def draw_lines(self) -> None:
        # Copy from previous assignment
        pass

    def draw_grid(self) -> None:
        # Copy from previous assignment
        pass

    def run(self) -> None:
        # Copy from previous assignment
        pass
