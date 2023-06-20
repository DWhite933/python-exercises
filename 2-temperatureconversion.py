# Converting between Celsius and Fahrenheit involves a basic calculation and provides a good exercise for writing functions that take in a numeric input and return a numeric output.
# This exercise tests your ability to use Python’s math operators and translate math equations into Python code.
# Write a convertToFahrenheit() function with a degreesCelsius parameter. This function returns the number of this temperature in degrees Fahrenheit. 
# Then write a function named convertToCelsius() with a degreesFahrenheit parameter and returns a number of this temperature in degrees Celsius.
# Use these two formulas for converting between Celsius and Fahrenheit:
#   Fahrenheit = Celsius × (9 / 5) + 32
#   Celsius = (Fahrenheit - 32) × (5 / 9)

def convertToFahrenheit(degreesCelsius : float):
    return degreesCelsius * (9/5) + 32.0
  

def convertToCelsius(degreesFahrenheit: float):
    return (degreesFahrenheit - 32.0) * (5/9)

# Test asserts
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15