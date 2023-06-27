#| A function can return a value.

# define a function to return a value
def cube(n):
    # calculate the cube
    n_cube = n ** 3
    
    #return this n_cube
    return n_cube

# call the function and recieve the returned value
num = 5
cube_of_num = cube(num)

# print the returned value assigned to the variable
print(cube_of_num)

# call the function within another function
print(cube(3))

#| Functions wich don't return values are called 'void'