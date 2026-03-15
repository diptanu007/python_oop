import math
class Shape:
    def __init__(self,border_thickness,border_color,location):
        self.border_thickness = border_thickness
        self.border_color = border_color
        self.location = location

    def __str__(self):
        return f"{self.__class__.__name__} ({self.border_thickness}, {self.border_color}, {self.location})"   

class Circle(Shape):
    def __init__(self,border_thickness,border_color,location,radius):
        super().__init__(border_thickness,border_color,location)
        self.radius = radius
    def __str__(self):
        return f"{super().__str__()}, {self.radius}"

    def area(self):
        return math.pi * self.radius **2
           
