import pytest
from puzzle import (
    Puzzle
)


dict_key = {
    'left': 276,
    'right': 275,
    'up': 273,
    'down': 274
}

dict_puzzle = {
    (0, 0): 0,  (1, 0): 1,  (2, 0): 2,  (3, 0): 3,
    (0, 1): 4,  (1, 1): 5,  (2, 1): 6,  (3, 1): 7,
    (0, 2): 8,  (1, 2): 9,  (2, 2): 10, (3, 2): 11,
    (0, 3): 12, (1, 3): 13, (2, 3): 14, (3, 3): 15
}

dict_puzzle_after_perm = {
    (0, 0): 0,  (1, 0): 1,  (2, 0): 2,  (3, 0): 3,
    (0, 1): 4,  (1, 1): 5,  (2, 1): 6,  (3, 1): 7,
    (0, 2): 8,  (1, 2): 9,  (2, 2): 10, (3, 2): 11,
    (0, 3): 12, (1, 3): 13, (2, 3): 15, (3, 3): 14
}


@pytest.fixture
def puzzle():
    screen = Puzzle(4, 4, 100)
    screen.squares = dict_puzzle
    screen.blank_square = (3, 3)
    return screen


grid_width = 4
grid_height = 4
square_size = 100

max_x = grid_width - 1
max_y = grid_height - 1


class TestPuzzle:
    def test_puzzle(self, puzzle):
        assert puzzle is not None

        assert puzzle.grid_width == grid_width
        assert puzzle.grid_height == grid_height
        assert puzzle.square_size == square_size
        assert puzzle.total_squares == grid_width*grid_height-1
        assert puzzle.squares == dict_puzzle
        assert puzzle.blank_square == (max_x, max_y)
        assert puzzle.solution == dict_puzzle

    def test_permute(self, puzzle):

        square_to_perm = (2, 3)
        puzzle.permute(square_to_perm)

        print(puzzle.squares)
        assert puzzle.squares == dict_puzzle_after_perm
        assert puzzle.blank_square == (2, 3)

    def test_is_in_grid(self, puzzle):
        square_internal = [(0, 0), (0, max_y), (max_x, 0), (max_x, max_y)]

        for square in square_internal:
            assert puzzle.is_in_grid(square) is True

        square_external = [(0, -1), (0, max_y+1), (-1, 0), (max_x+1, 0)]

        for square in square_external:
            assert puzzle.is_in_grid(square) is False

    def test_square_to_permute_left(self, puzzle):
        x, y = puzzle.square_to_permute((dict_key['left']))
        assert (x, y) == (puzzle.blank_square[0]+1, puzzle.blank_square[1])

    def test_square_to_permute_right(self, puzzle):
        x, y = puzzle.square_to_permute((dict_key['right']))
        assert (x, y) == (puzzle.blank_square[0]-1, puzzle.blank_square[1])

    def test_square_to_permute_up(self, puzzle):
        x, y = puzzle.square_to_permute((dict_key['up']))
        assert (x, y) == (puzzle.blank_square[0], puzzle.blank_square[1]+1)

    def test_square_to_permute_down(self, puzzle):
        x, y = puzzle.square_to_permute((dict_key['down']))
        assert (x, y) == (puzzle.blank_square[0], puzzle.blank_square[1]-1)
