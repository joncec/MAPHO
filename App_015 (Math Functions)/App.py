# For mathematical operations the module 'math' is used.
# Modules are any Python file 9.py) that include executable Python code.

# Import math module
import math

# See the module docs
print(math)

# See detailed docs (help() <- gives you detailed docs)
help(math)

# Any function can be called by -> .(dot) notation
#| Example A:

math.pi

#| Example B:
# What is the perimeter (circumference) of a circle having radius of 10cm?
# Perimeter = 2 * pi * r (radius)

# radius
r = 10

# perimeter
perimeter = 2 * math.pi * r
print(perimeter)

#| Example C:
# Calculate the sine of 30 degrees -> sin(30)

degree = 30

# calculate radian
radian = math.radians(degree)

print(radian)

"""
#| Incorrect usage example:

 sine = math.sin(degree)
 
 That is an incorrect usage of the function as according to help(math.sin)
 sin() works as following:
 
 sin(x,/)
    Return the sine of x (measured in radians).
    
The correct usage would be as follows:
"""
sine = math.sin(radian)
print(sine)

# Composition of Functions:

#| Chaining Functions
degree = 30
sine = math.sin(math.radians(degree))
print(sine)