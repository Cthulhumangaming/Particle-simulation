from view import *
import math

particles = []

sun = Particle(30, Vec(0,0), Vec(0,0), 1)
particles.append(sun)

planet = Particle(3, Vec(3,0), Vec(0,3), 0.5)
particles.append(planet)

simulation_loop(gravity, 0.00005, particles)
