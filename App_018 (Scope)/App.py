#| Scope is the region where the variables exist, it is determined by indentation.
#| Example:

# function scope
def scope_fn ():
    scope_var = 100
    print(scope_var)
    
# call the function
scope_fn()
#| Obs: Trying to reach 'scope_var' will result in an error as it only exists in scope_fn's scope.

#| Global Scope
short = 40
long = 60

# Defining function to use Global Scope variables:
def perimeter():
    area_of_rectangle = short * long
    print(area_of_rectangle)

# Calling the function:
perimeter()

#| Changing Global variables:
def change_globals(): # doesn't work in this case, read explanation below.
    short = 50
    print(short)
    
change_globals() 

#| Printing global variable again:
print(short)

"""
| Even though global variables can be acessed anywherer in the code, if changes are made within a function
| these changes will only occur within the function, as nothing has changed globally.
| If you want to change global variables you have to use global keywords.
"""
#| Example:

def change_globals():
    global short
    short = 50
    print(short)
    
#| By calling 'global' the global variable can be changed within the function.