# Abstract Classes and Methods
# Assignment: Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    
# Example

rectangle = Rectangle(5, 10)
print(f"Area of Rectangle: {rectangle.area()} meter square")  # Output: Area of Rectangle: 50