from view import *
import math

particles = []

sun = Particle(1000, Vec(0,0), Vec(0,0), 0.8)
particles.append(sun)

planet = Particle(0.002, Vec(-10,0), Vec(0,-15), 0.3)
particles.append(planet)

moon = Particle(0.0001, Vec(-10.001,0), Vec(0,0.1), 0.2)
particles.append(moon)

simulation_loop(gravity, 0.00005, particles)