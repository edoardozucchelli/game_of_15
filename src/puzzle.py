import pygame
from datetime import datetime

from src import puzzle_config as c
from src.grid_generator import create_legit_grid


pygame.init()

clock = pygame.time.Clock()


class Screen:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.display = pygame.display
        self.screen = self.display.set_mode((self.width, self.height))

        self.display.set_caption('Game of 15')


class Puzzle:
    def __init__(self, grid_width, grid_height, square_size):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.square_size = square_size
        self.total_squares = grid_width*grid_height-1
        self.total_moves = 0

        self.squares = create_legit_grid(self.grid_width, self.grid_height, self.total_squares)
        self.blank_square = self.find_blank_position()

        self.solution = {
            (x, y): i
            for i, (x, y)
            in enumerate((x, y) for y in range(grid_height) for x in range(grid_width))
        }

        self.time = None
        self.font = pygame.font.Font(None, 100)

    def find_blank_position(self):
        for key, value in self.squares.items():
            if value == self.total_squares:
                return key

    def is_completed(self):
        if self.squares == self.solution:
            return True
        return False

    def permute(self, square):
        self.squares[square], self.squares[self.blank_square] = self.squares[self.blank_square], self.squares[square]
        self.blank_square = square

    def is_in_grid(self, square):
        return 0 <= square[0] < self.grid_width and 0 <= square[1] < self.grid_height

    def square_to_permute(self, key):
        x, y = self.blank_square

        if key == pygame.K_LEFT:
            x, y = x+1, y
        elif key == pygame.K_RIGHT:
            x, y = x-1, y
        elif key == pygame.K_UP:
            x, y = x, y+1
        elif key == pygame.K_DOWN:
            x, y = x, y-1

        return x, y

    def event_handler(self, event):
        key = event.key
        square_to_permute = self.square_to_permute(key)

        if self.is_in_grid(square_to_permute):
            self.total_moves += 1
            self.permute(square_to_permute)

            if self.total_moves == 1:
                self.time = pygame.time.get_ticks()

    def draw(self, screen):
        for pos, num in self.squares.items():
            x, y = pos
            square = pygame.Rect(x*self.square_size, y*self.square_size,
                                 self.square_size, self.square_size)

            if num != self.total_squares:
                pygame.draw.rect(screen, c.RECT_COLOUR, square)
                pygame.draw.rect(screen, c.BORDER_COLOUR, square, c.BORDER_SIZE)

                text = self.font.render(str(num+1), 2, c.TEXT_COLOUR)
                screen.blit(text, (x*self.square_size, y*self.square_size))


class Game:
    def __init__(self):
        self.game_quit = False

        self.screen = Screen(c.SCREEN_WIDTH, c.SCREEN_HEIGHT)
        self.puzzle = Puzzle(grid_width=c.GRID_WIDTH, grid_height=c.GRID_HEIGHT, square_size=c.SIZE)

    def restart(self):
        return self.__init__()

    def draw_objects(self):
        self.puzzle.draw(self.screen.screen)

    def show_results(self):
        game_time_millisecond = pygame.time.get_ticks() - self.puzzle.time
        game_time_formatted = datetime.fromtimestamp(game_time_millisecond / 1000).strftime('%M:%S.%f')
        print("Puzzle completed in", self.puzzle.total_moves, "moves,", game_time_formatted, "minutes")

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit = True
            if event.type == pygame.KEYDOWN:
                self.puzzle.event_handler(event)
                if self.puzzle.is_completed():
                    self.show_results()
                    self.restart()

    def game_loop(self):
        self.screen.screen.fill(c.SCREEN_COLOUR)
        self.event_loop()
        self.draw_objects()
        self.screen.display.update()


def main():
    fps = c.FPS
    game = Game()

    while not game.game_quit:
        game.game_loop()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
  main()
