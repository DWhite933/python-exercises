# Area, perimeter, volume, and surface area are straightforward calculations. This exercise is similar to Exercise #2, “Temperature Conversion” 
# and Exercise #3, “Odd & Even.” Each function in this exercise is a simple calculation and return statement. However, area and volume are slightly
# more complicated because they involve multiple parameters. This exercise continues to challenge you to translate mathematical formulas into Python code.

# You will write four functions for this exercise. The functions area() and perimeter() have length and width parameters and the functions volume() and surfaceArea() have length, width, and height parameters.
# These functions return the area, perimeter, volume, and surface area, respectively.

# The formulas for calculating area, perimeter, volume, and surface area are based on the length (L), width (W), and height (H) of the shape:
#   area = L × W
#   perimeter = L + W + L + W
#   volume = L × W × H
#   surface area = (L × W × 2) + (L × H × 2) + (W × H × 2)

def area(length : int, width : int):
    return length * width

def perimeter(length : int, width : int):
    return (2 * length) + (2 * width)

def volume(length : int, width : int, height : int):
    return length * width * height

def surfaceArea(length : int, width : int, height : int):
    return (length * width * 2) + (length * height * 2) + (width * height * 2)

# test assertions
assert area(10, 10) == 100
assert area(0, 9999) == 0
assert area(5, 8) == 40
assert perimeter(10, 10) == 40
assert perimeter(0, 9999) == 19998
assert perimeter(5, 8) == 26
assert volume(10, 10, 10) == 1000
assert volume(9999, 0, 9999) == 0
assert volume(5, 8, 10) == 400
assert surfaceArea(10, 10, 10) == 600
assert surfaceArea(9999, 0, 9999) == 199960002
assert surfaceArea(5, 8, 10) == 340