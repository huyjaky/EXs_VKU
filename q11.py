class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year


def get_weekday_name(day, month, year):
    # Using Zeller's Congruence algorithm to find the day of the week
    if month < 3:
        month += 12
        year -= 1
    K = year % 100
    J = year // 100
    f = day + 13 * (month + 1) // 5 + K + K // 4 + J // 4 + 5 * J
    weekday = f % 7
    weekday_names = [
        "Saturday",
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
    ]
    return weekday_names[weekday]


def get_month_name(month):
    month_names = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    return month_names[month - 1]


def calculate_age(day, month, year):
    from datetime import datetime

    today = datetime.now()
    age = today.year - year - ((today.month, today.day) < (month, day))
    return age


# Example usage:
day, month, year = map(int, input("Enter your birthday (day month year): ").split())
date = Date(day, month, year)

weekday_name = get_weekday_name(date.day, date.month, date.year)
month_name = get_month_name(date.month)
age = calculate_age(date.day, date.month, date.year)

print(f"Weekday: {weekday_name}")
print(f"Month: {month_name}")
print(f"Age: {age}")
