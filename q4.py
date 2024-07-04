import random


def check_number():
    number = random.randint(-100, 100)
    if number > 0:
        sign = "positive"
    else:
        sign = "negative"

    if -99 <= number <= -10 or 10 <= number <= 99:
        digits = "two digits"
    else:
        digits = "not two digits"

    print(f"{number} is {sign} and has {digits}.")


check_number()
