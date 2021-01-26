import pathlib
import random

from typing import List, Optional, Tuple


Cell = Tuple[int, int]
Cells = List[int]
Grid = List[Cells]


class GameOfLife:
    
    def __init__(
        self,
        size: Tuple[int, int],
        randomize: bool=True,
        max_generations: Optional[float]=float('inf')
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1


    def create_grid(self, randomize: bool=False) -> Grid:
        def cell_val():
            return random.randrange(2) if randomize else 0

        self.grid = [[cell_val() for col in range(self.cell_width)] for row in range(self.cell_height)]

    def get_neighbours(self, cell: Cell) -> Cells:
        row, col = cell
        st_row = row - 1 + int(row == 0)
        st_col = col - 1 + int(col == 0)
        en_row = (row + 1) - int(row == self.cell_height - 1)
        en_col = (col + 1) - int(col == self.cell_width - 1)
        res = []
        for for_row in range(st_row, en_row + 1):
            for for_col in range(st_col, en_col + 1):
                if for_row == row and for_col == col:
                    continue
                res.append(self.grid[for_row][for_col])
        return res


    def get_next_generation(self) -> Grid:
        new_grid = [[0] * self.cell_width for row in range(self.cell_height)]
        for row in range(self.cell_height):
            for col in range(self.cell_width):
                neighbors = sum(self.get_neighbours((row, col)))
                alive = (self.grid[row][col] == 1)
                if alive:
                    if neighbors in [2, 3]:
                        new_grid[row][col] = 1
                else:
                    if neighbors == 3:
                        new_grid[row][col] = 1
        return new_grid




    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.grid
        self.grid = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """
        return  self.generations <= self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.grid != self.prev_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> 'GameOfLife':
        """
        Прочитать состояние клеток из указанного файла.
        """
        grid = []
        with open(filename) as file:
            for row in file:
                grid.append(list(row))
        return grid

    def save(filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """
        with open(filename) as file:
            for row in self.grid: