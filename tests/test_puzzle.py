import pytest

from src import puzzle_config as c
from src.puzzle import Screen, Puzzle, Game

dict_key = {
    'left': 276,
    'right': 275,
    'up': 273,
    'down': 274
}

c.SIZE = 100

c.GRID_WIDTH = 4
c.GRID_HEIGHT = 4

MAX_X = c.GRID_WIDTH - 1
MAX_Y = c.GRID_HEIGHT - 1

SCREEN_WIDTH = c.SIZE * c.GRID_WIDTH
SCREEN_HEIGHT = c.SIZE * c.GRID_HEIGHT


@pytest.fixture
def dict_puzzle():
    dict_puzzle = {
        (0, 0): 0,  (1, 0): 1,  (2, 0): 2,  (3, 0): 3,
        (0, 1): 4,  (1, 1): 5,  (2, 1): 6,  (3, 1): 7,
        (0, 2): 8,  (1, 2): 9,  (2, 2): 10, (3, 2): 11,
        (0, 3): 12, (1, 3): 13, (2, 3): 14, (3, 3): 15
    }
    return dict_puzzle


@pytest.fixture
def dict_puzzle_after_perm():
    dict_puzzle_after_perm = {
        (0, 0): 0,  (1, 0): 1,  (2, 0): 2,  (3, 0): 3,
        (0, 1): 4,  (1, 1): 5,  (2, 1): 6,  (3, 1): 7,
        (0, 2): 8,  (1, 2): 9,  (2, 2): 10, (3, 2): 11,
        (0, 3): 12, (1, 3): 13, (2, 3): 15, (3, 3): 14
    }
    return dict_puzzle_after_perm


@pytest.fixture
def screen():
    screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)
    return screen


@pytest.fixture
def puzzle(dict_puzzle):
    screen = Puzzle(c.GRID_WIDTH, c.GRID_HEIGHT, 100)
    screen.squares = dict_puzzle
    print(dict_puzzle)
    screen.blank_square = (MAX_X, MAX_Y)
    return screen


@pytest.fixture
def game():
    game = Game()
    return game


class TestScreen:
    def test_screen(self, screen):
        assert screen is not None
        assert screen.width == SCREEN_WIDTH
        assert screen.height == SCREEN_HEIGHT
        assert screen.screen.get_width() == SCREEN_WIDTH
        assert screen.screen.get_height() == SCREEN_HEIGHT
        assert screen.display.get_caption() == ('Game of 15', 'Game of 15')


class TestPuzzle:
    def test_puzzle(self, puzzle):
        assert puzzle is not None

        assert puzzle.grid_width == c.GRID_WIDTH
        assert puzzle.grid_height == c.GRID_HEIGHT
        assert puzzle.square_size == c.SIZE
        assert puzzle.total_squares == c.GRID_WIDTH * c.GRID_HEIGHT - 1
        assert puzzle.squares is not None
        assert puzzle.blank_square == (MAX_X, MAX_Y)
        assert puzzle.solution is not None

    def test_find_blank_position(self, puzzle):
        assert puzzle.find_blank_position() == (3, 3)

    def test_is_completed(self, puzzle, dict_puzzle_after_perm):
        assert puzzle.is_completed() is True
        puzzle.squares = dict_puzzle_after_perm
        assert puzzle.is_completed() is False

    def test_permute(self, puzzle, dict_puzzle_after_perm):

        square_to_perm = (2, 3)
        puzzle.permute(square_to_perm)

        print(puzzle.squares)
        assert puzzle.squares == dict_puzzle_after_perm
        assert puzzle.blank_square == (2, 3)

    def test_is_in_grid(self, puzzle):
        square_internal = [(0, 0), (0, MAX_Y), (MAX_X, 0), (MAX_X, MAX_Y)]

        for square in square_internal:
            assert puzzle.is_in_grid(square) is True

        square_external = [(0, -1), (0, MAX_Y + 1), (-1, 0), (MAX_X + 1, 0)]

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


class TestGame:
    def test_game(self, game):
        assert game is not None
        assert game.game_quit is False

        assert game.screen is not None
        assert game.puzzle is not None
