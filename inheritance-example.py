from classexample import Point

# just to test that Point was imported as expected
# a = Point(5, 5)
# print(a)


class ColorPoint(Point):
    # this is a class that inherits from Point!
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return f"{self.color}<{self.x}, {self.y}>"

# lets do 5 random color points
import random
colors = ["red", "blue", "green", "yellow", "purple", "cyan", "black", "white", "celadon", "xanadoo"]
color_points = []
for _ in range(5):
    color_point = ColorPoint(random.randint(1, 100),
                             random.randint(1, 100),
                             random.choice(colors))
    color_points.append(color_point)

print(color_points)

