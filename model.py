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
        self.charge = 0
    def inertial_move(self, dt):
        self.position += dt * self.velocity
    def apply_force(self, dt, f):
        self.velocity += dt * (1/self.mass) *f 
    def bounding_box(self):
        vec_bot_right = Vec(self.position.get_coords()[0] + self.radius, self.position.get_coords()[1] - self.radius)
        vec_top_left = Vec(self.position.get_coords()[0] - self.radius, self.position.get_coords()[1] + self.radius)
        return (vec_bot_right, vec_top_left)
    def set_charge(self, new_charge):
        self.charge = new_charge

#————————————————————————————————————————#
#---------------- Forces ----------------#
#————————————————————————————————————————#

def gravity(dt, particles, G = 1):
    for p1 in particles:
        f_g = Vec(0,0)
        for p2 in particles:
            if not p2 is p1:
                f_g += radius_force(p1, p2, p1.mass, p2.mass, G) 
        p1.apply_force(dt, f_g)

def collision(dt, particles, k = 100000.0):
    for p1 in particles:
        f = Vec(0, 0)
        for p2 in particles:
            if not p2 is p1: 
                r = (p2.position - p1.position).norm()
                if r < p2.radius + p1.radius:
                    f += k * (p2.radius + p1.radius - r)*(1/r)*(p1.position - p2.position)
                    # Neutralizing charges
                    p1_c = p1.charge
                    p2_c = p2.charge
                    new_charge = (p1_c+p2_c)/2
                    p1.set_charge(new_charge)
                    p2.set_charge(new_charge)
        p1.apply_force(dt, f)

def coulomb_force(dt, particles, k = 1):
    for p1 in particles:
        f_e = Vec(0,0)
        for p2 in particles:
            if not p2 is p1:
                f_e += radius_force(p1, p2, p1.charge, p2.charge, k) 
        p1.apply_force(dt, f_e)

def radius_force(p1, p2, p1_attribute, p2_attribute, const):
    f = const * (p1_attribute * p2_attribute)/((p2.position - p1.position).norm()**2)
    f_vec = f / (p2.position - p1.position).norm() * (p2.position - p1.position) 
    return f_vec