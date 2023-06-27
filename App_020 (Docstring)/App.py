#| Docstring is the given documentation on a function defined within it's source.
#| For help and information about a function call 'help(function)'
#| Example:

# define function
def example():
    print('Words and spaces')

# call help
help(example)

# defining a function with docstring
import math
def get_power(num, p):
    '''
    Calculates the power (p) of number (num).
    Parameters: int num, int p
    Returns: the given power of the number
    '''
    # calculate the power
    power = math.pow(num, p)
    
    # return the power
    return power

# get help with the created function
help(get_power)

#| In Python, objects have built-in methods and attributes, shortcuts allow us to acess these.
#| Example:

get_power.__doc__
print(get_power.__doc__)

#| Double underscores are used to acess special methods and attributes with predefined names.