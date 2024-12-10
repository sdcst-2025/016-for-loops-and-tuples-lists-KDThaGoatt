#Task 5
"""
Iterate through the list of numbers.
If the number is positive, determine the square root of the number.
State the number and the square root value
"""
import math

nums = (5,-2,12,-8,14,16)

for val in nums:
    if val > 0:
        s = math.sqrt(val)
        print(f"The square root of {val} is {s}")
    else:
        print(f"the square root of {val} is not possible")