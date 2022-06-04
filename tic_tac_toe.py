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
            c = 200 + 5 * ((x+y) % 2)
            col = (c, c, c)
            if board[x][y] is not "":
                col = COLORS[board[x][y].lower()]
            pygame.draw.rect(SCREEN, col,
                             (x_pos, y_pos, tile_size, tile_size))
            # draw_text(board[x][y], (0, 0, 0),
            #           (x_pos + tile_size / 2, y_pos + tile_size / 2))


def get_tile(mouse_pos):
    global tile_size
    return (int(mouse_pos[0] // tile_size), int(mouse_pos[1] // tile_size))


# CONSTANTS
WIDTH = 800
HEIGHT = 800
BACKGROUND = (0, 0, 0)
COLORS = {
    "a": (0, 0, 0),
    "b": (50, 0, 0),
    "c": (100, 0, 0),
    "d": (150, 0, 0),
    "e": (200, 0, 0),
    "f": (250, 0, 0),
    "g": (0, 50, 0),
    "h": (0, 100, 0),
    "i": (0, 150, 0),
    "j": (0, 200, 0),
    "k": (0, 250, 0),
    "l": (0, 0, 50),
    "m": (0, 0, 100),
    "n": (0, 0, 150),
    "o": (0, 0, 200),
    "p": (0, 0, 250),
    "q": (50, 50, 0),
    "r": (0, 50, 50),
    "s": (100, 100, 0),
    "t": (0, 100, 100),
    "u": (150, 150, 0),
    "v": (0, 150, 150),
    "w": (50, 0, 50),
    "x": (100, 0, 100),
    "y": (150, 0, 150),
    "z": (200, 0, 200),

}
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
SCREEN.fill(BACKGROUND)
update()

# Stuff
board = Board(8, 3, ["a", "i", "z"])
tile_size = WIDTH/len(board.board)

# Loop
running = True
reset_board = False

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
            if reset_board:
                board.reset()
                reset_board = False
            else:
                tile = get_tile(pygame.mouse.get_pos())
                if board.attempt_move(tile[0], tile[1]):
                    won, winner = board.check_win()
                    if won == 1:
                        print(winner + " won")
                        reset_board = True
                    elif won == 2:
                        print("draw")
                        reset_board = True

    update()


# Quit
print("Quitting")
pygame.quit()
