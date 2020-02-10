#Karl Schaller
#CIS 1051 - 002 Python
#Lab #10 - Lists and Strings

import math

def hasDoubleLetters(word):
    for i in range(len(word) - 1):
        if word[i] == word[i+1]:
            return True
    return False

def isPalindrome(word):
    return word == word[::-1]

def numberOfWords(string):
    count = 1
    for letter in string:
        if letter == " ":
            count = count + 1
    return count

def isSorted(intList):
    for i in range(len(intList) - 1):
        if intList[i+1] < intList[i]:
            return False
    return True

def roundAllUp(floatList):
    for i in range(len(floatList)):
        floatList[i] = math.ceil(floatList[i])
    return floatList

def generateTriangleNumbers(integer):
    triangleList = []
    for i in range(1, integer + 1):
        triangleNum = 0
        for j in range(1, i + 1):
            triangleNum = triangleNum + j
        triangleList.append(triangleNum)
    return triangleList

def reverseAll(stringList):
    for i in range(len(stringList)):
        reversedString = ""
        for j in range(len(stringList[i])-1, -1, -1):
            reversedString = reversedString + stringList[i][j]
        stringList[i] = reversedString

def minGap(intList):
    minGap = abs(intList[0] - intList[1])
    for i in range(1, len(intList) - 1):
        if minGap > abs(intList[i] - intList[i+1]):
            minGap = abs(intList[i] - intList[i+1])
    return minGap

def main():
    if (hasDoubleLetters("balloon")):
        print("balloon has double letters")
    else:
        print("balloon doesn't have double letters")
    if (hasDoubleLetters("test")):
        print("test has double letters")
    else:
        print("test doesn't have double letters")

    if (isPalindrome("radar")):
        print("radar is a palindrome")
    else:
        print("radar is not a palindrome")
    if (hasDoubleLetters("test")):
        print("test is a palindrome")
    else:
        print("test is not a palindrome")

    print("'hello, world' has: " + str(numberOfWords("hello, world")) + " word(s)")
    print("'test' has: " + str(numberOfWords("test")) + " word(s)")

    myList = [1, 3, 5, 7, 9]
    print(str(myList) + " is sorted: " + str(isSorted(myList)))
    myList = [3, 7, 5, 1, 9]
    print(str(myList) + " is sorted: " + str(isSorted(myList)))

    myList = [3.3, 4.32, 5.6685, 5.5, 2.2]
    print(str(myList) + " rounded up is : " + str(roundAllUp(myList)))

    print(str(generateTriangleNumbers(7)))

    stringList = ["banana", "radar", "test", "palindrome", "reverse"]
    print(str(stringList) + " reversed is: ")
    reverseAll(stringList)
    print(str(stringList))

    myList = [1, 3, 6, 7, 12]
    print("The min gap of " + str(myList) + " is: " + str(minGap(myList)))
    
if __name__ == "__main__":
    main()
