from view import *
import math

particles = []

sun = Particle(1000, Vec(0,0), Vec(0,0), 0.8)
particles.append(sun)

for i in range(1, 5):
    planet = Particle(0.001*i, i*Vec(-3,0), 1/i*Vec(0,-22), 0.3)
    particles.append(planet)

simulation_loop(gravity, 0.00005, particles, None)