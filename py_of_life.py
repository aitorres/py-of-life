import argparse
import os
import random
import sys
import time
from dataclasses import dataclass, field
from typing import Final

DISPLACEMENT_MATRIX: Final[set[tuple[int, int]]] = set(
    (i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]
) - {(0, 0)}


@dataclass
class Grid:
    height: int
    width: int
    grid: list[list[bool]] = field(default_factory=list)

    def init_random(self) -> None:
        assert self.height > 0 and self.width > 0

        self.grid = []
        for i in range(self.height):
            self.grid.append([])
            for _ in range(self.width):
                self.grid[i].append(bool(random.getrandbits(1)))

    def validate_grid_position(self, i: int, j: int) -> bool:
        return 0 <= i < self.height and 0 <= j < self.width

    def compute_cell_state(
        self, current_state: bool, neighbors_count: int
    ) -> bool:
        # Any live cell with two or three live neighbours lives on
        # to the next generation.
        if current_state and neighbors_count in [2, 3]:
            return True
        # Any dead cell with exactly three live neighbours becomes a
        # live cell, as if by reproduction.
        elif not current_state and neighbors_count == 3:
            return True
        # Any live cell with fewer than two live neighbours dies,
        # as if by underpopulation.
        # Any live cell with more than three live neighbours dies,
        # as if by overpopulation.
        else:
            return False

    def compute_next_generation(self) -> None:
        live_neighbors_counts: list[list[int]] = [[0] * self.width for _ in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                if self.grid[i][j]:
                    for x, y in DISPLACEMENT_MATRIX:
                        if self.validate_grid_position(i + x, j + y):
                            live_neighbors_counts[i + x][j + y] += 1

        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = self.compute_cell_state(self.grid[i][j], live_neighbors_counts[i][j])

    def print_grid(self) -> None:
        board_separator: Final[str] = " " + "＿" * (self.width + 1) + "\n"
        grid_str: str = ""

        grid_str += board_separator

        for i in range(self.height):
            grid_str += "| "

            for j in range(self.width):
                cell = "*" if self.grid[i][j] else " "
                grid_str += cell + " "

            grid_str += "|\n"

        grid_str += board_separator
        sys.stdout.write(grid_str)


def clear_screen() -> None:
    """
    Determines and runs the correct system command in order to
    clear the screen.
    """

    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="pyoflife",
        description="A Python implementation of Conway's Game of Life."
    )
    parser.add_argument("height", type=int, help="Height of the grid")
    parser.add_argument("width", type=int, help="Width of the grid")
    parser.add_argument(
        "iters", type=int, help="Amount of iterations / generations to play for"
    )

    args = parser.parse_args()

    height: int = args.height
    width: int = args.width
    iters: int = args.iters

    if any(x <= 0 for x in [height, width, iters]):
        sys.stdout.write(
            "ERROR: Please enter positive (> 0) values for width, height and iterations!"
        )
        sys.exit(1)

    grid = Grid(height, width)
    grid.init_random()

    for generation in range(iters):
        clear_screen()
        grid.print_grid()
        grid.compute_next_generation()
        sys.stdout.write(f"Generation {generation + 1} out of {iters}\n")
        time.sleep(0.05)


if __name__ == "__main__":
    main()
