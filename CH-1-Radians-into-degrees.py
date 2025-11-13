"""
1. Convert radians into degrees
Write a function in Python that accepts one numeric parameter. This parameter will be the measure of an angle in radians. 
The function should convert the radians into degrees and then return that value.

While you might find a Python library to do this for you, you should write the function yourself. 
One hint you get is that you’ll need to use Pi in order to solve this problem. You can import the value for Pi from Python’s math module.

"""

from math import pi

def randians_into_degrees(radian):
    pi_value = pi
    degrees = radian * 180 / pi

    return f' Converting {radian} radians into degrees we have: {degrees}°'


print(randians_into_degrees(pi/2))

