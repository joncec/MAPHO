# In Python, Strings are displayed via "double quotes" or 'single quotes', these should always match.
# Example:

string_double = "This is a double quote string"
print(string_double)

string_single = 'This is a single quote string'
print(string_single)

# Using quotes inside each other

single_in_double = " Big Boy Roy's Big Boy Toys"
print(single_in_double)

double_in_single = 'Jaalshem the Great said to the bard "I shall become the greatest wizard"'
print(double_in_single)


"""
In Python you can't do Arithmetic Operations on Strings (str).
Example:

'5' / '5'
    
"10" - "2" 

The only exceptional cases are + and * because they're interpreted differently.
Example:
"""

first = "Sunny"
second = "Days"

# Addition in Strings (Concatination)
print ( first + second)

print ('1' + first)

# Multiplication in Strings
print (4 * first)

print ( 2 * second)
