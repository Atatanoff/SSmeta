
import math


class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Point[x = {self.x}, y = {self.y}]"
    
def calculate_square(points):
    n = len(points)
    s = 0
    for i in range(n):
        point_a = points[i]
        point_b = points[(i+1)%n]
        s += point_a.x * point_b.y - point_b.x * point_a.y
    return 1/2 * abs(s)


if __name__ == '__main__':
    pass