from numpy import tile
import pygame
from board import Board

pygame.init()


def update():
    pygame.display.flip()


def draw_text(t, color, pos):
    global SCREEN
    font_size = 150
    my_font = pygame.font.Font(None, font_size)
    text = str(t)
    render_font = my_font.render(text, 1, color)
    text_rect = render_font.get_rect(center=pos)
    SCREEN.blit(render_font, text_rect)


def draw_board(board):
    global SCREEN
    global WIDTH
    global tile_size
    for x in range(len(board)):
        for y in range(len(board)):
            x_pos = x * tile_size
            y_pos = y * tile_size
            pygame.draw.rect(SCREEN, (200, 200, 200),
                             (x_pos, y_pos, tile_size, tile_size))
            draw_text(board[x][y], (0, 0, 0),
                      (x_pos + tile_size / 2, y_pos + tile_size / 2))


def get_tile(mouse_pos):
    global tile_size
    return (int(mouse_pos[0] // tile_size), int(mouse_pos[1] // tile_size))


# CONSTANTS
WIDTH = 600
HEIGHT = 600
BACKGROUND = (0, 0, 0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(BACKGROUND)
update()

# Stuff
board = Board(3, 3, ["x", "o"])
tile_size = WIDTH/len(board.board)

# Loop
running = True

print("Start")
while running:
    # Clear screen
    SCREEN.fill(BACKGROUND)
    draw_board(board.board)

    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.mouse.get_pressed()[0]:
            tile = get_tile(pygame.mouse.get_pos())
            if board.attempt_move(tile[0], tile[1]):
                won, winner = board.check_win()
                if won:
                    print(winner + " won")

    update()


# Quit
print("Quitting")
pygame.quit()
