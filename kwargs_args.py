# Calculates area of a rectangle (width & height) or a circle (radius)
import math


def calculate_area(**kwargs):
    if "width" in kwargs:
        return kwargs["width"] * kwargs["height"]
    if "radius" in kwargs:
        return (kwargs["radius"] ** 2) * math.pi


print(calculate_area(width=3, height=8))
print(calculate_area(radius=5))

# -----------------------------------
