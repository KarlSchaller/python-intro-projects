#Karl Schaller
#CIS 1051 - 002 Python
#Lab #3 - Loops

def bottlesOfBeer(numBottles):
    for bottles in range(numBottles, 0, -1):
        print(str(bottles) + " bottles of beer on the wall, " + str(bottles) + " bottles of beer")
        print("Take one down, pass it around, " + str(bottles-1) + " bottles of beer on the wall")
        print()
def multTable(size):
    row = ""
    for y in range(1, size+1):
        for x in range(1, size+1):
            row += str(x*y) + "\t"
        print(row)
        row = ""
def summationOfSquares(upToNum):
    sum = 0
    for x in range(1, upToNum+1):
        sum += x*x
    print(sum)
def hourglass():
    print('|""""""""""|')
    for x in range(8, 0, -2):
        print(" "*((10-x)//2) + "\\", end = "")
        for i in range(x):
            print(":", end = "")
        print("/")
    print("     ||")
    for x in range(2, 10, 2):
        print(" "*((10-x)//2) + "/", end = "")
        for i in range(x):
            print(":", end = "")
        print("\\")
    print('|""""""""""|')
def slashFigure(size):
    for row in range(size):
        print("\\"*(row*2)+"!"*(size*4-2-row*4)+"/"*(row*2))

def main():
    bottlesOfBeer(10)
    multTable(3)
    print()
    summationOfSquares(5)
    print()
    hourglass()
    print()
    slashFigure(4)
    print()
    slashFigure(6)
    print()
    slashFigure(7)

main()
