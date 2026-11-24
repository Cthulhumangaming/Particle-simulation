from view import *
from model import *
import random
import math

n = 5
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 8* random.random() * u 
    vel = 0 * u 
    p = Particle(1,pos,vel,0.5)
    p.charge = random.randint(-10, 10) / 10
    particles.append(p)

def forces(dt,particles):
    collision(dt, particles)
    coulomb_force(dt, particles)

simulation_loop(forces, 0.000005, particles, color_from_charge)