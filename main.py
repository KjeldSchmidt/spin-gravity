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

class ShellPoint:
    def __init__(self, x: float, y: float, v: Velocity, c: Point):
        self.x = x
        self.y = y
        self.v = v
        self.mass = 1
        self.c = c
        self.r = ((x-c.x)**2 + (y-c.y)**2)**0.5

    def update(self):
        direction_to_center = self.c.x - self.x, self.c.y - self.y
        h = (direction_to_center[0]**2 + direction_to_center[1]**2)**0.5
        force = 1

        a_c_x = direction_to_center[0]/h * force
        a_c_y = direction_to_center[1]/h * force

        self.v.x += a_c_x
        self.v.y += a_c_y

        self.x += self.v.x
        self.y += self.v.y

    def draw(self):
        app.fill(220, 13, 35)
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

c = Point(width/2, height/2)

judy = SmallMass(c.x, c.y + 100, 1, Velocity(1, 0))
shell = [ShellPoint(300, 300, Velocity(5, 0), c)]

def draw():
    app.background(255)
    app.fill(0)
    app.ellipse(c.x, c.y, 5, 5)
    judy.update()
    judy.draw()
    for shell_point in shell:
        shell_point.update()
        shell_point.draw()

while True:
   draw()
   app.redraw() # refresh the window


