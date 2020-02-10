#Karl Schaller
#CIS 1051 - 002 Python
#Lab #3 - Loops 2

def numVowels(word):
    numVowels = 0
    for letter in word.lower():
        if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
            numVowels += 1
    return numVowels
def numEvenDigits(number):
    numEven = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            numEven += 1
    return numEven
def threeDigArmstrong(number):
    sum = 0
    for digit in str(number):
        sum += int(digit)*int(digit)*int(digit)
    return sum == number
def riddler():
    for thousands in range(3, 12, 3):
        tens = thousands // 3
        for hundreds in range(0, 10):
            for ones in range(1, 11, 2):
                if (ones + tens + hundreds + thousands == 27):
                    if (ones != tens and ones != hundreds and ones != thousands and tens != hundreds and tens != thousands and hundreds != thousands):
                        return int(str(thousands) + str(hundreds) + str(tens) + str(ones))
def main():
    word = "balloons"
    print('"' + word + '"' + " has " + str(numVowels(word)) + " vowels")
    
    number = 123456789
    print(str(number) + " has " + str(numEvenDigits(number)) + " even digits")
    
    number = 371
    if (threeDigArmstrong(number)):
        print(str(number) + " is a Three Digit Armstrong Number")
    else:
        print(str(number) + " is not a Three Digit Armstrong Number")

    number = 123456788
    print(str(number) + " has " + str(numEvenDigits(number)) + " even digits")
    
    number = 407
    if (threeDigArmstrong(number)):
        print(str(number) + " is a Three Digit Armstrong Number")
    else:
        print(str(number) + " is not a Three Digit Armstrong Number")

    print("The Riddler plans to strike at " + str(riddler()) + " Pennsylvania Avenue")

main()
