#Karl Schaller
#CIS 1051 - 002 Python
#Lab #5 - Turtles and Loops

import turtle
import math

def olympics(aTurtle, size):
    aTurtle.pendown()
    width = size/5
    aTurtle.pensize(width)
    bluePos = aTurtle.position()
    yellowPos = bluePos + (size + width, -3*size)
    blackPos = yellowPos + (size + width, 3*size)
    greenPos = blackPos + (size + width, -3*size)
    redPos = greenPos + (size + width, 3*size)

    aTurtle.color("blue") #draw blue ring
    aTurtle.right(180)
    aTurtle.circle(size)
    aTurtle.penup()
    aTurtle.color("yellow") #draw yellow ring
    aTurtle.goto(yellowPos)
    aTurtle.right(180)
    aTurtle.pendown()
    aTurtle.circle(size)
    aTurtle.penup()
    aTurtle.color("black") #draw black ring
    aTurtle.goto(blackPos)
    aTurtle.right(180)
    aTurtle.pendown()
    aTurtle.circle(size)
    aTurtle.penup()
    aTurtle.color("green") #draw green ring
    aTurtle.goto(greenPos)
    aTurtle.right(180)
    aTurtle.pendown()
    aTurtle.circle(size)
    aTurtle.penup()
    aTurtle.color("red") #draw red ring
    aTurtle.goto(redPos)
    aTurtle.right(180)
    aTurtle.pendown()
    aTurtle.circle(size)
    aTurtle.penup()

    aTurtle.color("blue") #fix blue overlap
    aTurtle.goto(bluePos)
    aTurtle.pendown()
    aTurtle.circle(size, -135)
    aTurtle.penup()
    aTurtle.circle(size, 135)
    aTurtle.color("yellow") #fix yellow overlap
    aTurtle.goto(yellowPos + (0, size*2))
    aTurtle.pendown()
    aTurtle.circle(size, -45)
    aTurtle.penup()
    aTurtle.circle(size, 45)
    aTurtle.color("black") #fix black overlap
    aTurtle.goto(blackPos)
    aTurtle.pendown()
    aTurtle.circle(size, -135)
    aTurtle.penup()
    aTurtle.circle(size, 135)
    aTurtle.color("green") #fix green overlap
    aTurtle.goto(greenPos + (0, size*2))
    aTurtle.pendown()
    aTurtle.circle(size, -45)
    aTurtle.penup()
    aTurtle.circle(size, 45)
    
    aTurtle.right(180) #reset turtle to default values
    aTurtle.color("black")
    aTurtle.pensize(1)
    aTurtle.pendown()

def clock(aTurtle, size):
    aTurtle.penup()
    for i in range(12):
        aTurtle.forward(2*size/3)
        aTurtle.pendown()
        aTurtle.forward(size/6)
        aTurtle.penup()
        aTurtle.forward(size/6)
        aTurtle.stamp()
        aTurtle.right(180)
        aTurtle.forward(size)
        aTurtle.right(150)
    aTurtle.pendown()

def myInitials(aTurtle, size):
    aTurtle.write("KAS", True, "left", ("Arial", 20, "normal"))
    
    aTurtle.pendown()
    
    aTurtle.left(90) #begin K
    aTurtle.forward(size)
    aTurtle.right(180)
    aTurtle.forward(size/2)
    aTurtle.left(135)
    aTurtle.forward(size/2/math.cos(math.pi/4))
    aTurtle.right(180)
    aTurtle.forward(size/2/math.cos(math.pi/4))
    aTurtle.left(90)
    aTurtle.forward(size/2/math.cos(math.pi/4))
    aTurtle.left(45)

    aTurtle.left(70) #begin A
    aTurtle.forward(size/math.sin(7*math.pi/18))
    aTurtle.right(140)
    aTurtle.forward(size/math.sin(7*math.pi/18))
    aTurtle.right(180)
    aTurtle.forward(size/math.sin(7*math.pi/18)/2)
    aTurtle.left(70)
    aTurtle.forward(size/math.tan(7*math.pi/18))
    aTurtle.right(180)
    aTurtle.forward(size/math.tan(7*math.pi/18))
    aTurtle.right(70)
    aTurtle.forward(size/math.sin(7*math.pi/18)/2)
    aTurtle.left(70)
    
    aTurtle.forward(size/4) #begin S
    aTurtle.circle(size/4, 180)
    aTurtle.penup()
    aTurtle.right(90)
    aTurtle.forward(size/2)
    aTurtle.left(90)
    aTurtle.pendown()
    aTurtle.circle(size/4, 180)
    aTurtle.penup()
    aTurtle.left(90)
    aTurtle.forward(size/2)
    aTurtle.right(90)
    aTurtle.pendown()
    aTurtle.forward(size/4)

def drawShape(aTurtle, numSides, size):
    aTurtle.pendown()
    for side in range(numSides):
        aTurtle.forward(size/numSides)
        aTurtle.left(360/numSides)
        
def main():
    bob = turtle.Turtle()
    bob.shape("turtle")
    bob.speed(10)
    
    bob.penup()
    bob.goto(-350, 300)
    olympics(bob, 70)

    bob.penup()
    bob.goto(200, 200)
    clock(bob, 100)

    bob.penup()
    bob.goto(-300, -200)
    myInitials(bob, 100)

    bob.penup()
    bob.goto(200, -200)
    drawShape(bob, 8, 500)
    
    turtle.done()

main()
