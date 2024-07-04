def rectangle_perimeter_area(width, height):
    perimeter = 2 * (width + height)
    area = width * height
    return perimeter, area


width = int(input("Enter width: "))
height = int(input("Enter height: "))

perimeter, area = rectangle_perimeter_area(width, height)
print(f"Perimeter: {perimeter}, Area: {area}")
