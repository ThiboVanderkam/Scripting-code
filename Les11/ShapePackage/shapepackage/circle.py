from shape import Shape
import numpy as np
import turtle

class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return (self.radius ** 2) * np.pi
    def circumference(self):
        return 2 * self.radius * np.pi
    def draw(self):
        wn = turtle.Screen()
        t = turtle.Turtle()
        t.circle(self.radius)
        wn.mainloop()
