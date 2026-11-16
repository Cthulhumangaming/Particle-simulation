import math

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return "(", self.x, ",", self.y, ")"
    
    def __rmul__(self, factor):
        return Vector(self.x * factor, self.y * factor)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def norm(self):
        out = math.sqrt(self.x**2 + self.y**2)
        return out

    def get_coords(self):
        return (self.x,self.y)
        

def dot(u,v):
    return u.x * v.x + u.y * v.y

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
