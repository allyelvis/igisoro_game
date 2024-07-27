import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
BOARD_ROWS, BOARD_COLS = 4, 8
CELL_SIZE = 60
PADDING = 20
SEEDS_PER_HOLE = 2

# Colors
BG_COLOR = (245, 222, 179)
BOARD_COLOR = (139, 69, 19)
SEED_COLOR = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Igisoro")

# Board class
class Board:
    def __init__(self):
        self.holes = [[SEEDS_PER_HOLE for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

    def draw(self):
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                x = PADDING + col * CELL_SIZE
                y = PADDING + row * CELL_SIZE
                pygame.draw.rect(screen, BOARD_COLOR, (x, y, CELL_SIZE, CELL_SIZE))
                seeds = self.holes[row][col]
                font = pygame.font.Font(None, 36)
                text = font.render(str(seeds), True, SEED_COLOR)
                text_rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
                screen.blit(text, text_rect)

    def sow(self, row, col):
        seeds_to_sow = self.holes[row][col]
        self.holes[row][col] = 0
        current_row, current_col = row, col
        while seeds_to_sow > 0:
            current_col += 1
            if current_col == BOARD_COLS:
                current_col = 0
                current_row = (current_row + 1) % BOARD_ROWS
            if current_row != row or current_col != col:
                self.holes[current_row][current_col] += 1
                seeds_to_sow -= 1

# Main function
def main():
    board = Board()
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                row = (mouse_y - PADDING) // CELL_SIZE
                col = (mouse_x - PADDING) // CELL_SIZE
                if 0 <= row < BOARD_ROWS and 0 <= col < BOARD_COLS:
                    board.sow(row, col)

        screen.fill(BG_COLOR)
        board.draw()
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
