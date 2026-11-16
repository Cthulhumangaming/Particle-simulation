from tkinter import *
from model import *

def to_canvas_coords(canvas, u):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
    tu = u.get_coords()
    return h/20 * Vec(tu[0]+w/2, -tu[1]+h/2)
 
root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()
o = canvas.create_oval(80, 30, 140, 150, fill="blue")
input()

# Task (10/12): Define a new function move_oval_to(o, u1, u2)
def move_oval_to(o, u1, u2):
    u1_cords = to_canvas_coords(canvas, u1)
    u2_cords = to_canvas_coords(canvas, u2)

    canvas.coords(o, u1_cords[0], u1_cords[1], u2_cords[0], u2_cords[1])

# Task (11/12): Define a new function create_oval(canvas, particle)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
