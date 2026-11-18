from view import *
import math

n = 20
particles = []
for i in range(n):
    theta = i*2*math.pi/n
    u = Vec(math.cos(theta),math.sin(theta))
    pos = 3 * u
    vel = -3 * u 
    particles.append(Particle(1,pos,vel,0.2))

def no_force(dt,particles):
    pass

simulation_loop(collision, 0.00005, particles)
