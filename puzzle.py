import pygame
import puzzle_config as c


pygame.init()


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

        self.squares = {
            (x, y): i
            for i, (x, y)
            in enumerate((x, y) for y in range(grid_height) for x in range(grid_width))
        }

        self.blank_square = list(self.squares.keys())[-1]
        self.solution = self.squares
        self.font = pygame.font.Font(None, 100)

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
            self.permute(square_to_permute)

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

    def draw_objects(self):
        self.puzzle.draw(self.screen.screen)

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_quit = True
            if event.type == pygame.KEYDOWN:
                self.puzzle.event_handler(event)

    def game_loop(self):
        self.screen.screen.fill(c.SCREEN_COLOUR)
        self.event_loop()
        self.draw_objects()
        self.screen.display.update()


def main():
    clock = pygame.time.Clock()
    fps = c.FPS
    game = Game()

    while not game.game_quit:
        game.game_loop()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
  main()
