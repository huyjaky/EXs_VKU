import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def euclidean_distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


def manhattan_distance(p1, p2):
    return abs(p1.x - p2.x) + abs(p1.y - p2.y)


def cosine_distance(p1, p2):
    dot_product = p1.x * p2.x + p1.y * p2.y
    magnitude_p1 = math.sqrt(p1.x**2 + p1.y**2)
    magnitude_p2 = math.sqrt(p2.x**2 + p2.y**2)
    return 1 - (dot_product / (magnitude_p1 * magnitude_p2))


# Example usage:
x1, y1 = map(int, input("Enter coordinates of the first point (x1 y1): ").split())
x2, y2 = map(int, input("Enter coordinates of the second point (x2 y2): ").split())

p1 = Point(x1, y1)
p2 = Point(x2, y2)

euclidean = euclidean_distance(p1, p2)
manhattan = manhattan_distance(p1, p2)
cosine = cosine_distance(p1, p2)

print(f"Euclidean Distance: {euclidean}")
print(f"Manhattan Distance: {manhattan}")
print(f"Cosine Distance: {cosine}")
