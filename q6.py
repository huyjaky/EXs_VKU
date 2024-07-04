import math


def clock_angle(hour, minute):
    hour_angle = (hour % 12 + minute / 60) * 30
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    angle = min(angle, 360 - angle)
    radian = math.radians(angle)
    return angle, radian


hour = int(input("Enter hour: "))
minute = int(input("Enter minute: "))
angle, radian = clock_angle(hour, minute)
print(f"Angle: {angle} degrees, Radian: {radian}")
