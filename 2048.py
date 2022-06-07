from tkinter import Frame, Label, CENTER

import codes
import design as d


class Game2048(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.grid()
        self.master.title('2048')
        self.master.bind("<Key>", self.KEY_DOWN)
        self.commands = {d.KEY_UP: codes.move_up, d.KEY_DOWN: codes.move_down,
                         d.KEY_LEFT: codes.move_left, d.KEY_RIGHT: codes.move_right
                        }
        
        self.grid_cells = []
        self.init_grid()
        self.init_matrix()
        self.update_grid_cells()

        self.mainloop()

    def init_grid(self):
        background = Frame(self, bg=d.BACKGROUND_COLOR_GAME,
                           width=d.SIZE, height=d.SIZE)
        background.grid()

        for i in range(d.GRID_LEN):
            grid_row = []
            for j in range(d.GRID_LEN):
                cell = Frame(background, bg=d.BACKGROUND_COLOR_CELL_EMPTY,
                             width=d.SIZE / d.GRID_LEN,
                             height=d.SIZE / d.GRID_LEN)
                cell.grid(row=i, column=j, padx=d.GRID_PADDING,
                          pady=d.GRID_PADDING)
                t = Label(master=cell, text="",
                          bg=d.BACKGROUND_COLOR_CELL_EMPTY,
                          justify=CENTER, font=d.FONT, width=5, height=2)
                t.grid()
                grid_row.append(t)

            self.grid_cells.append(grid_row)


    def init_matrix(self):
        self.matrix = codes.start_game()
        codes.add_2(self.matrix)
        codes.add_2(self.matrix)

    def update_grid_cells(self):
        for i in range(d.GRID_LEN):
            for j in range(d.GRID_LEN):
                new_number = self.matrix[i][j]
                if new_number == 0:
                    self.grid_cells[i][j].configure(
                        text="", bg=d.BACKGROUND_COLOR_CELL_EMPTY)
                else:
                    self.grid_cells[i][j].configure(text=str(
                        new_number), bg=d.BACKGROUND_COLOR_DICT[new_number],
                        fg=d.TEXT_COLOR_DICT[new_number])
        self.update_idletasks()

    def KEY_DOWN(self, event):
        key = repr(event.char)
        if key in self.commands:
            self.matrix, changed = self.commands[repr(event.char)](self.matrix)
            if changed:
                codes.add_2(self.matrix)
                self.update_grid_cells()
                changed = False
                if codes.get_current_state(self.matrix) == 'WON':
                    self.grid_cells[1][1].configure(
                        text="You", bg=d.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Win!", bg=d.BACKGROUND_COLOR_CELL_EMPTY)
                if codes.get_current_state(self.matrix) == 'LOST':
                    self.grid_cells[1][1].configure(
                        text="You", bg=d.BACKGROUND_COLOR_CELL_EMPTY)
                    self.grid_cells[1][2].configure(
                        text="Lose!", bg=d.BACKGROUND_COLOR_CELL_EMPTY)



gamegrid = Game2048()
