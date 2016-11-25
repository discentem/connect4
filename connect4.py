import tkinter as tk
import numpy as np


class Space(tk.Canvas):
    def __init__(self, Board, width, row, column):
        self.board = Board
        # Sets width of each square on the board
        self.width = width
        # Stores coordinates of this square in the grid
        self.row = row
        self.column = column
        # tag is a combo of row and column for convenience
        self.tag = (self.row, self.column)
        # Instantiate the superclass, Canvas
        super().__init__(width=self.width, height=self.width)
        # Stores color of circle
        self.color = None
        # Sets background and highlight color of each square
        self.config(background="yellow", highlightbackground="black",
                    highlightthickness=.5)
        # Creates clickable area -- runs self.clicked() when clicked
        self.bind("<Button-1>", self.clicked)

        # Draws circle for this square
        inset = 6
        self.circle = self.create_oval(self.width/inset, self.width/inset,
                                       self.width - self.width/inset,
                                       self.width - self.width/inset)

    # Calls drop_piece on this space's Board
    def clicked(self, event):
        self.board.drop_piece(self.row, self.column)


class Board(tk.Tk):

    def __init__(self, rows=6, cols=7,
                 square_width=80, player_colors=['red', 'green'],
                 num_to_win=4):

        # Sets number of rows
        self.rows = rows
        # Sets number of columns
        self.cols = cols
        # Square width
        self.square_width = square_width
        # List of colors for player1/2 pieces
        self.p_colors = player_colors
        # Num of adjacent pieces needed to win
        self.num_to_win = num_to_win
        # Player 1's turn at start
        self.player = 1
        # False until someone wins
        self.gameover = False

        # Intialize Tk frame
        super().__init__()
        # Set Tk title
        self.title("Connect 4")
        # Makes the Tk (window) size static
        self.resizable(width=False, height=False)
        # Set up visual grid and board tracking
        self.setup()

    def setup(self):
        # List where spaces will be stored
        self.grid = []
        # CLI list which tracks where pieces are for debugging and win checking
        self.cli_grid = []
        for x in range(0, self.rows):
            row = []
            cli_row = []
            for y in range(0, self.cols):
                s = Space(self, self.square_width, x, y)
                # arranges visual grid
                s.grid(row=x, column=y)
                # adds Space object to row
                row.append(s)
                # adds blank space to CLI matrix
                cli_row.append(" ")
            # Completes 2d list of Space objects
            self.grid.append(row)
            # Completes 2d list of CLI representation of board
            self.cli_grid.append(cli_row)

        self.cli_grid = np.array(self.cli_grid)

    def print_cli_grid(self, reverse=False):
        # Print CLI matrix
        if reverse:
            for row in np.fliplr(self.cli_grid):
                print(row)
        else:
            for row in self.cli_grid:
                print(row)
        print('\n')

    def drop_piece(self, row, col):
        # Tries to fill spaces bottom to top until it finds blank space
        for i in range(self.rows-1, -1, -1):
            space = self.grid[i][col]
            c1 = space.itemcget(1, 'fill') == self.p_colors[0]
            c2 = space.itemcget(1, 'fill') == self.p_colors[1]
            # If space does not have either player's piece...
            if not(c1) and not(c2):
                if self.player == 1:
                    space.itemconfig(1, fill=self.p_colors[0])
                    space.color = space.itemcget(1, 'fill')
                    self.player = -1
                elif self.player == -1:
                    space.itemconfig(1, fill=self.p_colors[1])
                    space.color = space.itemcget(1, 'fill')
                    self.player = 1
                break

        self.cli_grid[i][col] = str(self.grid[i][col].itemcget(1, 'fill'))[0]
        self.print_cli_grid()
        self.print_cli_grid(reverse=True)

        self.check_win(space.tag)
        print('clicked:', row, col)
        print('dropped:', space.tag)

    def check_win(self, tag):
        row = tag[0]
        col = tag[1]
        for color in self.p_colors:
            vert = self.check_vertical_win(col, color)
            horizontal = self.check_horizontal_win(row, color)
            diag1 = self.check_diagonal_win(row, col, color)
            if vert:
                print("vert", color)
            if horizontal:
                print("horizontal", color)
            if diag1:
                print("diag", color)

    def check_vertical_win(self, col, color):
        count = 0
        for r in range(0, self.rows):
            if self.cli_grid[r][col] == color[0]:
                count += 1
            else:
                count = 0
            if count >= self.num_to_win:
                return True

    def check_horizontal_win(self, row, color):
        count = 0
        for c in range(0, self.cols):
            if self.cli_grid[row][c] == color[0]:
                count += 1
            else:
                count = 0
            if count >= self.num_to_win:
                return True

    def checksub(self, list, sublist):
        count = 0
        for i in range(len(list)):
            if list[i] in sublist:
                count += 1
            else:
                count = 0
            if count >= len(sublist):
                return True

    def check_diagonal_win(self, row, col, color, direction='\ '):
        if direction == '\ ':
            diag = np.diag(self.cli_grid, col-row)
        win = [color[0]] * self.num_to_win

        if self.checksub(diag, win):
            return True


board = Board(square_width=50)
board.mainloop()
