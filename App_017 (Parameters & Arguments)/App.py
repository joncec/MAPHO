#| Parameters are inputs provided to the function during function call.

#| Defining a functions wich takes a parameter:
def print_square(number):
    # get the square
    sqr = number**2
    
    # print sqr
    print(sqr)

#| Calling the funtion:
print_square(3)
#Obs. An error will be caused if an invalid/null value is given as a parameter.

print_square(20)

print_square(6)

"""
| Defining a function that takes two parameters:
| Parameters: short, long
| Function will calculate and print the area of the rectangle.
"""
def area_of_rectangle (short, long):
    # calculating area and assigning it to a value
    area = short * long
    
    # print the area
    print(area)
    
#| Calling the function:
area_of_rectangle (4,6)

#| Calling it with variables as parameters:
s = 5
u = 9

area_of_rectangle (s,u)

"""
| Let's create a parametric function simmilar to student_name
| It will take in the first and last name, then when called, prints the whole name.
"""
def human_firstname (first):
    print("First Name: " + first)
    
def human_lastname (last):
    print("Last Name: " + last)
    
def human_fullname (first, last):
    human_firstname (first)
    human_lastname (last)
    
#| Calling the function with it's parameters:
first = "Benjamin"
last = "Jirhan"

human_fullname(first, last)
    
#| Creating another parametric wich takes in an Integer then returns it as a String:

def human_age (age):
    print("Age: " + str(age))
    
#| Creating a function to call both previous functions

def human_data (first, last, age):
    human_fullname (first, last)
    human_age (age)

#| Calling the new function:
human_data(first = "Roger", last = "Banks", age = 95)
