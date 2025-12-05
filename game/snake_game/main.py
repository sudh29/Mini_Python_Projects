from tkinter import *
import setting
import utils
from cell import Cell

root = Tk()
# settings
root.configure(bg="green")
root.geometry(f"{setting.WIDTH}x{setting.HEIGHT}")
root.title("MINESWEEPER GAME")
root.resizable(False, False)

top_frame = Frame(root, bg="green", width=setting.WIDTH, height=utils.height_per(25))
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame, bg="green", fg="white", text="MINESWEEPER GAME", font=("", 48)
)
game_title.place(x=utils.width_per(25), y=0)

left_frame = Frame(
    root, bg="green", width=utils.width_per(25), height=utils.height_per(75)
)
left_frame.place(x=0, y=utils.height_per(25))

center_frame = Frame(
    root, bg="green", width=utils.width_per(75), height=utils.height_per(75)
)
center_frame.place(x=utils.width_per(25), y=utils.height_per(25))


for x in range(setting.GRID_SIZE):
    for y in range(setting.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_oject(center_frame)
        c.cell_btn_object.grid(column=x, row=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines()
# run window
root.mainloop()
