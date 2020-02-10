#Karl Schaller
#CIS 1051 - 002 Python
#Turtle

import turtle

def fractal(x, y, size, angle, number, current, r, g, b):
    if (current < number):
        bob = turtle.Turtle()
        bob.hideturtle()
        bob.color(r, g, b)
        bob.speed(0)
        bob.penup()
        bob.setpos(x, y)
        bob.setheading(angle)
        bob.pendown()
        bob.forward(size)
        fractal(bob.xcor(), bob.ycor(), 2*size/3, bob.heading() - 30, number, current + 1, (number-1)*r/number, (number-1)*g/number, (number-1)*b/number)
        fractal(bob.xcor(), bob.ycor(), 2*size/3, bob.heading() + 30, number, current + 1, (number-1)*r/number, (number-1)*g/number, (number-1)*b/number)
    
def main():
    #fractal(0, 0, 100, 0, 6, 0, 0, 1, 0)
    #fractal(0, 0, 100, 90, 6, 0, 0, 1, 0)
    #fractal(0, 0, 100, 180, 6, 0, 0, 1, 0)
    #fractal(0, 0, 100, 270, 6, 0, 0, 1, 0)
    fractal(0, 300, 200, 270, 9, 0, 0, 1, 0)
    turtle.done()
    
main()
