import random
import os
from dataclasses import dataclass, field
from typing import Final

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

    def compute_next_generation(self) -> None:
        new_grid: list[list[bool]] = []
        displacement_matrix: list[list[int]] = set(
            (i, j) for i in [-1, 0, 1] for j in [-1, 0, 1]
        ) - {(0, 0)}

        for i in range(self.height):
            new_grid.append([])
            for j in range(self.width):
                cell = self.grid[i][j]
                live_neighbors_count = sum(
                    [
                        int(self.grid[i + x][j + y])
                        for (x, y) in displacement_matrix
                        if 0 <= (i + x) < self.height
                        and 0 <= (j + y) < self.width
                    ]
                )

                if cell and live_neighbors_count in [2, 3]:
                    new_grid[i].append(True)
                elif not cell and live_neighbors_count == 3:
                    new_grid[i].append(True)
                else:
                    new_grid[i].append(False)

        self.grid = new_grid

    def print_grid(self) -> None:
        board_separator: Final[str] = " " + "＿" * (self.width + 1)

        print(board_separator)

        for i in range(self.height):
            print("|", end=" ")

            for j in range(self.width):
                cell = "*" if self.grid[i][j] else " "
                print(cell, end=" ")

            print("|")

        print(board_separator)


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
    raise NotImplementedError()


if __name__ == "__main__":
    main()
