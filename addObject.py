class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)


point = Point(10, 2)
point2 = Point(3, 4)
point3 = point + point2
print(point3.x, point3.y)
