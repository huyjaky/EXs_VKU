import math


def solve_quadratic(a, b, c):
    discriminant = b**2 - 4 * a * c
    print(f"Discriminant: {discriminant}")

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Two solutions: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"One solution: {root}")
    else:
        print("No real solutions")


# Example usage:
solve_quadratic(1, 5, 6)
