import math

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"({self.x},{self.y})"
    def __rmul__(self, factor):
        return Vec(self.x * factor, self.y * factor)
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y)
    def norm(self):
        out = math.sqrt(self.x**2 + self.y**2)
        return out
    def get_coords(self):
        return (self.x, self.y)
        
def dot(u,v):
    return u.x * v.x + u.y * v.y

class Particle:
    def __init__(self, mass, position, velocity, radius):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.radius = radius
    def inertial_move(self, dt):
        self.position += dt * self.velocity
    def apply_force(self, dt, f):
        self.velocity += dt * (1/self.mass) *f 
    def bounding_box(self):
        vec_bot_right = Vec(self.position.get_coords()[0] + self.radius, self.position.get_coords()[1] - self.radius)
        vec_top_left = Vec(self.position.get_coords()[0] - self.radius, self.position.get_coords()[1] + self.radius)
        return (vec_bot_right, vec_top_left)

###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################
