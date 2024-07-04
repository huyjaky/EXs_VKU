def convert_length(cm):
    decimeter = cm / 10
    inch = cm / 2.54
    return decimeter, inch


# Example usage:
cm = float(input("Enter number with cm unit: "))
decimeter, inch = convert_length(cm)
print(f"{cm} cm = {decimeter} dm = {inch} inches")
