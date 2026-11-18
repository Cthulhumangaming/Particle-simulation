from view import *
import math

n = 5
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 5 * u
    vel = -10 * u 
    particles.append(Particle(1,pos,vel,1))
particles.pop()

def no_force(dt,particles):
    pass

simulation_loop(collision, 0.000005, particles)
