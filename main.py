import math

from processing_py import *

width = 800
height=800
app = App(width,height) # create window: width, height

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Velocity ({self.x}, {self.y})"

class ShellPoint:
    def __init__(self, x: float, y: float, c: Point, f_c: float):
        self.x = x
        self.y = y
        self.m = 1
        self.f_c = f_c
        self.c = c
        self.v = self.calculate_initial_stable_velocity()
        self.rainbow = rainbow()

    def calculate_initial_stable_velocity(self):
        direction_to_center = self.c.x - self.x, self.c.y - self.y
        h = (direction_to_center[0]**2 + direction_to_center[1]**2)**0.5

        f_c_x = (direction_to_center[0]/h)**2 * self.f_c
        f_c_y = (direction_to_center[1]/h)**2 * self.f_c


        r = ((self.x-self.c.x)**2 + (self.y-self.c.y)**2)**0.5
        v_x = ((abs(f_c_x)/self.m) * r) ** 0.5
        v_y = ((abs(f_c_y)/self.m) * r) ** 0.5

        return Velocity(v_y, -v_x)


    def update(self):
        # print(f"Before: {self.x}")
        direction_to_center = self.c.x - self.x, self.c.y - self.y
        h = (direction_to_center[0]**2 + direction_to_center[1]**2)**0.5
        force = self.f_c

        a_c_x = direction_to_center[0]/h * force
        a_c_y = direction_to_center[1]/h * force

        self.v.x += a_c_x
        self.v.y += a_c_y

        self.x += self.v.x
        self.y += self.v.y
        # print(f"After: {self.x}")

    def draw(self):
        app.fill(*next(self.rainbow))
        app.noStroke()
        app.circle(self.x, self.y, 5)


class SmallMass:
    def __init__(self, x: int, y: int, m: int, v: Velocity):
        self.x = x
        self.y = y
        self.m = m
        self.v: Velocity = v

    def update(self):
        self.x += self.v.x
        self.y += self.v.y

    def draw(self):
        app.fill(40, 35, 180)
        app.circle(self.x, self.y, self.m*10)

def rainbow():
    h = 0
    inc = 0.0025
    while True:
        yield h, 1, 1
        h += inc
        if h >= 1:
            h %= 1

c = Point(width/2, height/2)

judy = SmallMass(c.x, c.y + 100, 1, Velocity(1, 0))
f_c = 0.1

shell = [
    ShellPoint(c.x, y, c, f_c) for y in range(15, 400, 7)
]

def draw():
    app.ellipse(c.x, c.y, 5, 5)
    judy.update()
    # judy.draw()
    for shell_point in shell:
        shell_point.update()
        shell_point.draw()

app.background(255)
app.fill(0)
app.colorMode(HSB, 1, 1, 1)
while True:
    draw()
    app.redraw() # refresh the window


