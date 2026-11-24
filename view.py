from tkinter import *
from model import *
from model import *
import time

def lerp(x, a, b):
    return (x+b)/(b-a)

def to_canvas_coords(canvas, u):
    h = canvas.winfo_reqheight()
    w = canvas.winfo_reqwidth()
    tu = u.get_coords()
    return Vec(h/20*tu[0]+w/2, -h/20*tu[1]+h/2)

def color_from_charge(p):
    def to_hex(c):
        h = hex(c)[2:]
        if len(h) == 1:
            h = '0'+h
        return h
    r = int(lerp(p.charge, -1, 1) * 255)
    b = int((1-lerp(p.charge, -1, 1)) * 255)

    return f'#{to_hex(r)}00{to_hex(b)}'
 
root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()
#o = canvas.create_oval(80, 30, 140, 150, fill="blue")

def move_oval_to(o, u1, u2):
    u1_cords = to_canvas_coords(canvas, u1)
    u2_cords = to_canvas_coords(canvas, u2)

    canvas.coords(o, u1_cords.get_coords()[0], u1_cords.get_coords()[1], u2_cords.get_coords()[0], u2_cords.get_coords()[1])

def create_oval(canvas, particle, color_of):
    o = canvas.create_oval(0, 0, 0, 0, fill=color_of(particle))
    move_oval_to(o, particle.bounding_box()[0], particle.bounding_box()[1])
    return o

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
def simulation_loop(f, timestep, particles, color_of):
    if not color_of:
        color_of = lambda particle : 'blue'
    ovals = {}
    for p in particles:
        ovals[p] = create_oval(canvas, p, color_of)
    tm1 = time.time()
    while True:
        f(timestep, particles)
        for p in particles:
            p.inertial_move(timestep)
            canvas.itemconfig(ovals[p], fill=color_of(p))
            move_oval_to(ovals[p], p.bounding_box()[0], p.bounding_box()[1])

        t = time.time()
        if t - tm1 > 1/30:
            tm1 = t
            canvas.update()