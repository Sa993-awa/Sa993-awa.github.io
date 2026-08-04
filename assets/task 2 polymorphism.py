from abc import ABC,abstractmethod

# Abstract base class for all shapes
# It defines a common method area() that must be implemented by subclasses


class shape(ABC):                               # Abstract method: every shape class must provide its own area calculation
    @abstractmethod
    def area(self):
        pass

                                              # Circle class inherits from the abstract shape class
                                              # It calculates the area of a circle using the given radius

class Circle(shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):                            # Method to calculate and return the area of the circle
        return 3.14 * self.radius*self.radius 
    
                                          # Rectangle class inherits from the abstract shape class
                                          # It calculates the area of a rectangle using length and width
class Rectangle(shape):
     def  __init__(self,length,width):
         self.length = length
         self.width = width


     def area(self):                          # Method to calculate and return the area of the regtancle 
        return self.length * self.width

circle = Circle(5)                            # Creating an object of Circle with radius 5
rectangle = Rectangle(5,7)                    # Creating an object of Rectangle with length 5 and width 7

print("Circle area:",circle.area())
print("Rectangle area:",rectangle.area())     # Displaying calculated areas of both shapes