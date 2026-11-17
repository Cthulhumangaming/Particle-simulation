from tkinter import *
from model import *
from model import *
import time

def to_canvas_coords(canvas, u):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
    tu = u.get_coords()
    return Vec(h/20*tu[0]+w/2, -h/20*tu[1]+h/2)
 
root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()
#o = canvas.create_oval(80, 30, 140, 150, fill="blue")

def move_oval_to(o, u1, u2):
    u1_cords = to_canvas_coords(canvas, u1)
    u2_cords = to_canvas_coords(canvas, u2)

    canvas.coords(o, u1_cords.get_coords()[0], u1_cords.get_coords()[1], u2_cords.get_coords()[0], u2_cords.get_coords()[1])

def create_oval(canvas, particle):
    blueness = max(0, min(255, round(255/30*(30-particle.mass))))
    hexblue = hex(blueness)[2:]
    if len(hexblue) == 1:
        hexblue = '0' + hexblue
    o = canvas.create_oval(0, 0, 0, 0, fill=f'#0000{hexblue}')
    move_oval_to(o, particle.bounding_box()[0], particle.bounding_box()[1])
    return o

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles):
    ovals = {}
    for p in particles:
        ovals[p] = create_oval(canvas, p)
    tm1 = time.time()
    while True:
        f(timestep, particles)
        for p in particles:
            p.inertial_move(timestep)
            move_oval_to(ovals[p], p.bounding_box()[0], p.bounding_box()[1])

        t = time.time()
        if t - tm1 > 1/30:
            tm1 = t
            canvas.update()
