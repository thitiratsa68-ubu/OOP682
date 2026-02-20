from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> None:
        print("Drawing...")

def render(obj:Drawable):
    obj.draw() # ไม่ต้องสืบทอดจาก Drawable แค่มี method draw ก็พอ
    
render(Drawable())