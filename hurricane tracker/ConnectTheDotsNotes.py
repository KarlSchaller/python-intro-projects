#Karl Schaller
#CIS 1051 - 002 Python
#Lab #8 - Hurricane Tracker

import turtle

if __name__ == "__main__":
    lines = open("z.txt", "r").readlines()
    bob = turtle.Turtle()
    for dots in lines:
        dots = dots.strip()
        dots = dots.split("),")

        bob.penup()
        bob.speed(2)
        for dot in dots:
            dot = dot.replace("(", "")
            dot = dot.replace(")", "")
            coords = dot.split(",")
            x = int(coords[0]) * 23.5
            y = int(coords[1]) * 23.5
            bob.goto(x, y)
        
