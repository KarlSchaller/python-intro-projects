#Karl Schaller
#Intro to Problem Solving and Programming - Python
#Lab#2-Mini Programs

def threeSort():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    if num2 < num1:
        temp = num1
        num1 = num2
        num2 = temp
    if num3 < num2:
        temp = num2
        num2 = num3
        num3 = temp
    print(str(num1) + " " + str(num2) + " " + str(num3))
def temperature():
    celsius = float(input("Enter a temperature in Celsius: "))
    farenheit = celsius * 9 / 5 + 32
    print(str(celsius) + " degrees Celsius = " + str(farenheit) + " degrees Farenheit")
def secondsToHours():
    totalSeconds = int(input("Enter a number of seconds: "))
    minutes = totalSeconds // 60
    seconds = totalSeconds % 60
    hours = minutes // 60
    minutes %= 60
    print(str(totalSeconds) + " seconds = " + str(hours) + " hours, " + str(minutes) + " minutes, and " + str(seconds) + " seconds.")

threeSort()
temperature()
secondsToHours()
