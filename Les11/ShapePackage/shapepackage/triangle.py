from .shape import Shape #De punt voor shape is om een relatief pad aan te geven
import math as m
import numpy as np
import turtle

class Triangle(Shape):
    def __init__(self, s):
        self.side = s
    def area(self):
        height = m.sqrt(self.side**2 - ((self.side/2)**2))
        return self.side * height / 2
    def circumference(self):
        return 3*self.side
    def draw(self):
        wn = turtle.Screen()
        t = turtle.Turtle()
        for i in range(0,3):
            t.forward(self.side)
            t.left(120)
        wn.mainloop()


tr = Triangle(50)
tr.draw()