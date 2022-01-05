class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eg__(self, point2):
        return self.x == point2.x and self.y == point2.y

    def __gt__(self, point2):
        return self.x > point2.x and self.y > point2.y

    def __add__(self, point2):
        return Point(self.x + point2.x, self.y + point2.y)


point1 = Point(10, 20)
point2 = Point(11, 22)
point3 = point1 + point2
print(point3.x, point3.y)
