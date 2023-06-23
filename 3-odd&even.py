# Determining if a number is even or odd is a common calculation that uses the modulo operator. Like Exercise #2, “Temperature Conversion,” the functions for this exercise’s solution functions can be as little as one line long.
# This exercise covers the % modulo operator, and the technique of using modulo-2 arithmetic to determine if a number is even or odd.
# Write two functions, isOdd() and isEven(), with a single numeric parameter named number. The isOdd() function returns True if number is odd and False if number is even. 
# The isEven() function returns the True if number is even and False if number is odd. Both functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered an even number.

def isEven(num : int):
    """ This funciton checks if a number is even """
    return num % 2 == 0

def isOdd(num : int):
    """ This function checks if a number is odd"""
    return num % 2 == 1

if __name__ == '__main__':
    # Test asserts
    assert isOdd(42) == False
    assert isOdd(9999) == True
    assert isOdd(-10) == False
    assert isOdd(-11) == True
    assert isOdd(3.1415) == False
    assert isEven(42) == True
    assert isEven(9999) == False
    assert isEven(-10) == True
    assert isEven(-11) == False
    assert isEven(3.1415) == False