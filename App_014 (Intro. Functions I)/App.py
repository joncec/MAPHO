""""
Function is a special code fragment written to perform a specific task that only runs when called.
Functions may have parameters (arguments) and they may return a value back.
Functions prevent code duplications.

> calling a function with parameters:
    function_name(parameter_1, parameter_2)

> calling a function without parameters:
    function_name()
"""

# Example of Functions:

#| type() -> returns the type of the given argument
type (42)

type('a moody afternoon')

#| int() -> converts the given argument to int
int(5.68)

int (100)
# Obs: int('something') doesn't work as 'something' is a String and cannot be an Integer.

#| str() -> casts the given argument into string.
str(45)

str(4.57)

str('Guimblesmack')

#| float() -> casts the given argument into float
float(12)

float('4')

num = '-78'
float(num)

# Obs: num('78-') wouldn't work as it is a String and cannot be a float (because of where the "-" is).
