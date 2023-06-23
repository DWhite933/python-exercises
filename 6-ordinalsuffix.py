# While cardinal numbers refer to the size of a group of objects like “four apples” or “1,000 tickets”, ordinal numbers refer to the place of an object in an ordered sequence like “first place” or “30th birthday”. 
# This exercise involves numbers but is more an exercise in processing text than doing math.

# In English, ordinal numerals have suffixes such as the “th” in “30th” or “nd” in “2nd”. Write an ordinalSuffix() function with an integer parameter named number and returns a string of the number with its ordinal suffix. 
# For example, ordinalSuffix(42) should return the string '42nd'. #You may use Python’s str() function to convert the integer argument to a string. Python’s endswith() string method could be useful for this exercise,
# but to maintain the challenge in this exercise, don’t use it as part of your solution.

def ordinalSuffix(number):
    # convert number to str
    numStr = str(number)

    # 11-13 have th suffix
    if numStr[-2:] in ('11', '12', '13'):
        return numStr + 'th'
    
    # 1 has st suffix
    if numStr[-1:] == '1':
        return numStr + 'st'
    
    # 2 has nd suffix
    if numStr[-1] == '2':
        return numStr + 'nd'
    
    # 3 has rd suffix
    if numStr[-1] == '3':
        return numStr + 'rd'
    
    # all other numbers end with th
    return numStr + 'th'
    
if __name__ == '__main__':

    # test asserts
    assert ordinalSuffix(0) == '0th'
    assert ordinalSuffix(1) == '1st'
    assert ordinalSuffix(2) == '2nd'
    assert ordinalSuffix(3) == '3rd'
    assert ordinalSuffix(4) == '4th'
    assert ordinalSuffix(10) == '10th'
    assert ordinalSuffix(11) == '11th'
    assert ordinalSuffix(12) == '12th'
    assert ordinalSuffix(13) == '13th'
    assert ordinalSuffix(14) == '14th'
    assert ordinalSuffix(101) == '101st'
