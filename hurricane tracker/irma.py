#Karl Schaller
#CIS 1051 - 002 Python
#Lab #8 - Hurricane Tracker

import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()
    
    # your code to animate Irma here
    t.speed(7)
    data = open("data/irma.csv", "r").readlines()

    data[0] = data[1]
    t.penup()
    t.goto(float(data[0].split(",")[3]), float(data[0].split(",")[2]))
    t.pendown()
        
    for line in data:
        line = line.split(",")
        #print(line)
        t.goto(float(line[3]), float(line[2]))
        if int(line[4]) >= 157:
            t.color("red")
            t.write('5')
        elif int(line[4]) >= 130:
            t.color("orange")
            t.write('4')
        elif int(line[4]) >= 111:
            t.color("yellow")
            t.write('3')
        elif int(line[4]) >= 96:
            t.color("green")
            t.write('2')
        elif int(line[4]) >= 74:
            t.color("blue")
            t.write('1')
        else:
            t.color("white")
        t.width(int(line[4])/8)
        
    turtle.done()

if __name__ == "__main__":
    irma()
