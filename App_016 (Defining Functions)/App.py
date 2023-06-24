#| Without parameters:
def function_name():
    print("My first function")
    
#| Calling the function:
function_name()

#| Python used indentation for scoping, indentation can be created with 'tab' or '4  space'.

#| Student Data
print("Name: John Doe")
print("Age: 24")
print("Language: Python")

#| Student data necessary again, what should you do?

#| Define functions for student data:
 
def student_age():
    print("Age: 24")
    
def student_language():
    print("Language: Python")
    
#| Creating two separate functions to display the student's name separately if need be:
def student_firstname():
    print("John")
    
def student_lastname():
    print("Doe")

def student_name():
    student_firstname()
    student_lastname()
    
def student_data():
    student_name()
    student_age()
    student_language()

#| Printing Student Data again:
student_data()

'''
|Executionn flow:
first_line
| Then it moves on, if it encounters a function call
|first it goes into that function, executes it, waits for it to finish then returns back.
second_line
| And so on, whenever it encounters a functions it goes through that process.
'''