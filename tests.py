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

if __name__ == '__main__':
    unittest.main()