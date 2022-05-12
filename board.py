import pygame


class Board:
    players = []
    turn = 0

    board_size = 0
    board = [[]]
    win_num = -1

    def __init__(self, size, win_amount, players) -> None:
        # Win condition
        self.board_size = size
        self.win_num = win_amount
        # Create board
        self.board = []
        for x in range(size):
            col = []
            for y in range(size):
                col.append("")
            self.board.append(col)

        # Make sure empty square is not a player
        if "" not in players:
            self.players = players
        else:
            raise Exception("Invalid player")

    def attempt_move(self, x, y) -> bool:
        if self.board[x][y] != "":
            return False

        self.board[x][y] = self.players[self.turn]
        self.turn = (self.turn + 1) % len(self.players)
        return True

    def check_win(self) -> bool:

        # Check horizontal
        for x in range(self.board_size):
            for y in range(self.board_size):
                base_plr = self.board[x][y]
                win_h = True
                win_v = True
                win_d = True
                for w in range(self.win_num):
                    if x + w < self.board_size:
                        if self.board[x + w][y] != base_plr:
                            win_h = False
                    if y + w < self.board_size:
                        if self.board[x][y + w] != base_plr:
                            win_v = False
                    if x + w < self.board_size and y + w < self.board_size:
                        if self.board[x][y + w] != base_plr:
                            win_d = False
                if win_h or win_v or win_d:
                    return True
        return False
