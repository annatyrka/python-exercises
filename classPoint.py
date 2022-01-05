class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Print ({self.x},{self.y})")


point = Point(1, 2)
point.draw()

name = Point("Anna", "Tyrka")
name.draw()
