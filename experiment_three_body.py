from view import *
import math
from random import random

particles = []

# Randomly creates different three-body scenarios.
# Most scenarios are quite uninteresting
for i in range(3):
    mass = random()*30 + 1
    position = Vec(8*(random()*2 - 1), 8*(random()*2 - 1))
    velocity = Vec(10*(random()*2 - 1), 10*(random()*2 - 1))
    radius = mass/30
    particle = Particle(mass, position, velocity, radius)
    particles.append(particle)


simulation_loop(gravity, 0.00005, particles)