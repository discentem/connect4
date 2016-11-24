import tkinter as tk


class Space(tk.Canvas):
    def __init__(self, board, width, row, column, height=0):
        self.board = board
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        if self.height == 0:
            self.height = self.width

        # instantiate Canvas
        super().__init__(width=self.width, height=self.height)
        self.color = None
        # set board colors
        self.config(background="yellow", highlightbackground="black",
                    highlightthickness=.5)
        # create button
        self.bind("<Button-1>", self.clicked)
        # add to parent grid
        self.grid(row=self.row, column=self.column)

        inset = 6
        self.circle = self.create_oval(self.width/inset, self.height/inset,
                                       self.width - self.width/inset,
                                       self.height - self.height/inset)

    def clicked(self, event):
        self.board.drop_piece(self.row, self.column)


class Board(tk.Tk):

    def __init__(self, rows=6, cols=7,
                 square_width=80, square_height=0,
                 player_colors=['red', 'green']):

        self.rows = rows
        self.cols = cols
        self.square_width = square_width
        self.square_height = square_height
        self.p_colors = player_colors

        self.player = 1

        super().__init__()
        self.resizable(width=False, height=False)
        self.grid = []
        self.cli_grid = []
        for x in range(0, rows):
            row = []
            cli_row = []
            for y in range(0, cols):
                s = Space(self, square_width, x, y, height=self.square_height)
                row.append(s)
                cli_row.append("")
            self.grid.append(row)
            self.cli_grid.append(cli_row)

    def print_cli_grid(self):
        for row in self.cli_grid:
            print(row)
        print('\n')

    def drop_piece(self, row, col):
        for i in range(self.rows-1, -1, -1):
            space = self.grid[i][col]
            c1 = space.itemcget(1, 'fill') == self.p_colors[0]
            c2 = space.itemcget(1, 'fill') == self.p_colors[1]
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
        self.check_win(row, col)

    def check_win(self, row, col, num_to_win=4):
        for color in self.p_colors:
            # vertical
            count = 0
            for r in range(0, self.rows):
                if self.cli_grid[r][col] == color[0]:
                    count += 1
                else:
                    count = 0
                if count >= num_to_win:
                    print("vert!", color)
                    count = 0
            # horizontal
            count = 0
            for c in range(0, self.cols):
                if self.cli_grid[row][c] == color[0]:
                    count += 1
                else:
                    count = 0
                if count >= num_to_win:
                    print("horizontal!", color)
                    count = 0


board = Board()
board.mainloop()
