#bad idea: subclassing to change behavior of base class

class rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
class square(rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.height = height
        self.width = height
def resize_rectangle(rect: rectangle, new_width: float, new_height: float):
    rectangle.set_width(new_width)
    rectangle.set_height(new_height)
    return rectangle.width * rectangle.height