from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def resize(self, new_width: float, new_height: float):
        raise NotImplementedError("Subclasses must implement this method")
    
    @abstractmethod
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class rectangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    
    def resize(self, new_width: float, new_height: float):
        self.width = new_width
        self.height = new_height
    
    def area(self):
        return self.width * self.height
    
class square(shape):
    def __init__(self, side):
        self.side = side
    
    def resize(self, new_width: float, new_height: float):
        self.side = new_width
    
    def area(self):
        return self.side * self.side

def resize(shape: shape, new_width: float, new_height: float):
    return shape.set_width(new_width), shape.set_height(new_height)

rect = rectangle(4, 5)
print("Original rectangle area:", rect.area(4, 5))