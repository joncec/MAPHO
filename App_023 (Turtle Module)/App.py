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
import math

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
       
# calling the square function 
square ( 200, False)

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
    
# calling the polygon function utilizing named parameters
polygon ( d = 100, n = 8, is_clear = True)

# draw a circle
def circle(r, is_clear):
    '''
    This function draws a circle.
    Parameters:
        int r : radius
    Return: None (void)
    '''
    if is_clear == True:
        clear()
        
    # defining the perimeter > total distance drawn
    perimeter = 2 * math.pi * r
    
    # defining how many steps needed to draw the circle by dividing 360 degrees by the angle of an arc.
    steps = int(360 / 10)
    
    # distance > distance travelled by the pen in each arc
    distance = perimeter / steps
    polygon (d = distance, n = steps, is_clear = is_clear)
    
circle(200, True)
    
# experimenting with circles
for i in range (1, 8):
    circle(i*25, False)
    

# star
def star(d, n, is_clear, color):
    """
    This function draws a fixed size star with 5 points.

    Args:
        int d : distance (side size)
        int n : number of points
        is_clear (bool): clear screen
        str color : the color of the filling
    """
    # resetting screen
    if is_clear == True:
        clear()
        
    # line color / pen color
    t.color("black")
    
    # start filling
    t.fillcolor(color)
    t.begin_fill()
    
    #angle of 5 point star
    angle = 180 / n
    angle = 180 - angle
    
    for i in range(n):
        t.fd(d)
        t.lt(angle)
     
    # end filling   
    t.end_fill()
        
star(100, 9, True, "blue")

#  last statement before closure
turtle.mainloop()
# restart kernel after closing turtle