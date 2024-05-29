# Functions

import math

def area_of_circle(radius = 0):
    """Retruns the area of the circle with given radius"""
    return math.pi * (radius ** 2)


def volume(radius = 0):
    """returns the volume of the sphere with given radius"""
    return (4 / 3) * math.pi * (radius ** 3)


def area_of_triangle(base = 0, height = 0):
    """Returns the area of the triangle with given base and height"""
    return 0.5 * base * height


def cm(feet = 0, inches = 0):
    """Converts a length from feet and inches to"""
    inches_to_cm = inches * 2.54
    feet_to_cm = feet * 12 * 2.54
    return inches_to_cm + feet_to_cm


