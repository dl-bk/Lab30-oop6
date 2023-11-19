# Використовуючи поняття множинного успадкування,
# створіть клас «Коло, поміщене в квадрат».

class Square:
    def __init__(self, size) -> None:
        self.size = size
    
class Circle:
    def __init__(self, radius) -> None:
        self.radius = radius
    
class CircleInSquare(Circle, Square):
    def __init__(self, sq_size, c_radius) -> None:
        super().__init__(c_radius)
        Square.__init__(self, sq_size)


c_sq = CircleInSquare(12, 6)