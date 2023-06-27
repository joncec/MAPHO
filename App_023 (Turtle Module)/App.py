'''
> turtle.forward(distance)
> t.fd(distance)

Parameters: int/float : distance

Move the turtle forward by the specified distance, in the direction the turtle is headed.

> turtle.back(distance)
> t.bk(distance)
> turtle.backward(distance)
Parameters: int/float : distance

Move the turtle backward by distance, opposite to the direction the turtle is headed. Do not change the turtle’s heading.

> turtle.right(angle)
> t.rt(angle)
Parameters: int/float : angle

Turn turtle right by angle units. (Units are by default degrees, but can be set via the degrees() and radians() functions.) Angle orientation depends on the turtle mode, see mode().

turtle.left(angle)
t.lt(angle)
Parameters int/float : angle

Turn turtle left by angle units. (Units are by default degrees, but can be set via the degrees() and radians() functions.) Angle orientation depends on the turtle mode, see mode().
'''
# import the module
import turtle

t = turtle.Turtle()

def clear():
    # clears the screen, alternative: turtle.resetscreen()
    t.clear()

# draw a square
def square(d, is_clear):
    """
    This function draws a square.
    Parameters:
        int d : distance (lenght)
        bool is_clear : if the screen needs to be reset
    Return: None
    """
    if is_clear == True:
        clear()
        
    for i in range(4):
        t.fd(d)
        t.lt(90)

# for i in range (10):
#    square(i * 20, False)

# draw a polygon
def polygon(d, n, is_clear):
    '''
    This function draws a polygon.
    Parameters: int d : distance (lenght) 
                int n : number of sides
                bool is_clear : if the screen needs to be reset.
    Return: None
    '''
    if is_clear == True:
        clear()
        
    # angle
    angle = 360 / n
    
    # polygon
    for i in range (n):
        t.fd(d)
        t.lt(angle)

#  last statement before closure
turtle.mainloop()
# restart kernel after closing turtle