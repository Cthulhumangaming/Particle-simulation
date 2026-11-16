import math

# Task (2/12): Define a class Vec

# Task (3/12): Additionally define a function dot(u, v)

# Task (4/12): Create a class Particle
class Particle:
    def __init__(self, mass, position, velocity, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
    def inertiaL_move(self, dt):
        self.position += dt * self.velocity
    def apply_force(self, dt, f):
        self.velocity += dt * f/self.mass
    
    
    

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)

##########################################
### NB. Tasks 7-8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################
