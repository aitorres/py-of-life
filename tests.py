import unittest

from py_of_life import Grid

class TestPyOfLife(unittest.TestCase):

    def test_init_random(self):
        grid = Grid(5, 10)
        self.assertEqual(grid.grid, [])

        grid.init_random()
        self.assertNotEqual(grid.grid, [])
        self.assertEqual(len(grid.grid), 5)
        for row in grid.grid:
            self.assertEqual(len(row), 10)

    def test_compute_cell_state(self):
        grid = Grid(10, 10)

        for cell, neighbors in [
            (False, 3),
            (True, 2),
            (True, 3),
        ]:
            self.assertTrue(
                grid.compute_cell_state(cell, neighbors)
            )

        for cell, neighbors in [
            (False, 0),
            (False, 2),
            (False, 4),
            (True, 0),
            (True, 1),
            (True, 4),
        ]:
            self.assertFalse(
                grid.compute_cell_state(cell, neighbors)
            )

    def test_validate_grid_position(self):
        grid = Grid(10, 10)

        for i, j in [
            (0, 0),
            (1, 2),
            (0, 5),
            (7, 3),
            (9, 9),
        ]:
            self.assertTrue(grid.validate_grid_position(i, j))

        for i, j in [
            (-1, 0),
            (-1, -1),
            (3, -1),
            (0, 10),
            (10, 10),
            (15, 2),
        ]:
            self.assertFalse(grid.validate_grid_position(i, j))

    def test_compute_next_generation(self):
        # General test
        grid_1 = Grid(5, 5)
        grid_1.grid = [
            [False, True, False, False, False],
            [False, True, True, False, False],
            [True, False, False, True, False],
            [True, True, False, False, False],
            [True, False, False, False, True]
        ]
        grid_1.compute_next_generation()
        self.assertEqual(
            grid_1.grid,
            [
                [False, True, True, False, False],
                [True, True, True, False, False],
                [True, False, False, False, False],
                [True, True, False, False, False],
                [True, True, False, False, False]
            ]
        )

        # Test: No spontaneous generation
        grid_2 = Grid(3, 3)
        grid_2.grid = [
            [False, False, False],
            [False, False, False],
            [False, False, False]
        ]
        grid_2.compute_next_generation()
        self.assertEqual(
            grid_2.grid,
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ]
        )

        # Test: Underpopulation
        grid_3 = Grid(3, 3)
        grid_3.grid = [
            [False, False, True],
            [False, False, False],
            [False, False, True]
        ]
        grid_3.compute_next_generation()
        self.assertEqual(
            grid_3.grid,
            [
                [False, False, False],
                [False, False, False],
                [False, False, False]
            ]
        )

        # Test: Overpopulation
        grid_4 = Grid(2, 3)
        grid_4.grid = [
            [True, True, True],
            [False, True, True],
        ]
        grid_4.compute_next_generation()
        self.assertEqual(
            grid_4.grid,
            [
                [True, False, True],
                [True, False, True],
            ]
        )

        # Test: reproduction
        grid_5 = Grid(2, 3)
        grid_5.grid = [
            [True, False, True],
            [False, True, False],
        ]
        grid_5.compute_next_generation()
        self.assertEqual(
            grid_5.grid,
            [
                [False, True, False],
                [False, True, False],
            ]
        )

if __name__ == '__main__':
    unittest.main()