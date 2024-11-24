import pygame
from game_logic import CheckersGame

pygame.init()

# Window setup
WIN = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Checkers AI")
FPS = 60

# Global objects
game = CheckersGame()

# Render board and pieces
def draw_board(win, board):
    win.fill((255, 255, 255))  # White background
    for row in range(8):
        for col in range(8):
            color = (0, 0, 0) if (row + col) % 2 == 0 else (255, 255, 255)
            pygame.draw.rect(win, color, (col * 100, row * 100, 100, 100))
            piece = board[row][col]
            if piece != " ":
                piece_color = (255, 0, 0) if piece == 'r' else (0, 0, 0)
                pygame.draw.circle(win, piece_color, (col * 100 + 50, row * 100 + 50), 40)

# Main game loop
def main():
    clock = pygame.time.Clock()
    running = True

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                # Handle clicks (move pieces, etc.)

        draw_board(WIN, game.board)
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()