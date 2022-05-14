import pygame
from board import Board
from time import sleep as wait

pygame.init()


def update():
    pygame.display.flip()


def draw_text(t, color, pos, font_size=150, white_back=False):
    global SCREEN
    global COLORS
    my_font = pygame.font.Font(None, font_size)
    text = str(t)
    if text.lower() in COLORS:
        color = COLORS[text.lower()]
    if white_back:
        render_font = my_font.render(text, 1, color, (255, 255, 255))
    else:
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
            # if board[x][y] is not "":
            #     col = COLORS[board[x][y].lower()]
            pygame.draw.rect(SCREEN, col,
                             (x_pos, y_pos, tile_size, tile_size))
            draw_text(board[x][y], (0, 0, 0),
                      (x_pos + tile_size / 2, y_pos + tile_size / 2))
    
   


def get_tile(mouse_pos):
    global tile_size
    return (int(mouse_pos[0] // tile_size), int(mouse_pos[1] // tile_size))

def render_board():
    global SCREEN
    global board
    SCREEN.fill(BACKGROUND)
    draw_board(board.board)
    draw_text(board.players[board.turn], (0,0,0), (10, 10), font_size=25)
# CONSTANTS
WIDTH = 600
HEIGHT = 600
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
board = Board(3, 3, ["X", "O", "A"])
tile_size = WIDTH/len(board.board)

# Loop
running = True
reset_board = False

can_click = True
# render = True

print("Start")
while running:
    # Clear screen
    if not reset_board:
        render_board()

    # Get events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif pygame.mouse.get_pressed()[0] and can_click:
            can_click = False
            if reset_board:
                board.reset()
                reset_board = False
            else:
                tile = get_tile(pygame.mouse.get_pos())
                if board.attempt_move(tile[0], tile[1]):
                    won, winner = board.check_win()
                    if won == 1:
                        print(winner + " won")
                        render_board()
                        draw_text(winner + " WINS", (0, 0, 0), (WIDTH/2, HEIGHT/2), white_back=True)
                        update()
                        reset_board = True
                        #wait(1)
                    elif won == 2:
                        print("draw")
                        render_board()
                        draw_text("Draw", (0, 0, 0), (WIDTH/2, HEIGHT/2), white_back=True)
                        update()
                        reset_board = True
        elif not pygame.mouse.get_pressed()[0]:
            can_click = True

    if not reset_board:
        update()


# Quit
print("Quitting")
pygame.quit()
