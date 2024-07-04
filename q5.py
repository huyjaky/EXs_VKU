import random


def normalize_number():
    number = random.randint(10, 150)
    normalized = (number - 10) / (150 - 10)
    print(f"Original number: {number}, Normalized: {normalized}")


normalize_number()
