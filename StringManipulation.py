#Karl Schaller
#CIS 1051 - 002 Python
#Lab #6 - Pig Latin

def findFirstVowel(string):
    for i in range(len(string)):
        if string[i].lower() == "a" or string[i].lower() == "e" or string[i].lower() == "i" or string[i].lower() == "o" or string[i].lower() == "u":
            return i
    return len(string) - 1

def convertToPigLatin(string):
    if findFirstVowel(string) == 0:
        return string[1:] + string[0] + "way"
    else:
        return string[findFirstVowel(string):] + string[0:findFirstVowel(string)] + "ay"

def reverse(string):
    output = ""
    for i in range(len(string) - 1, -1, -1):
        output = output + string[i]
    return output

def ROT13(string):
    output = ""
    for letter in string.lower():
        output = output + chr((ord(letter) - 97 + 13) % 26 + 97)
    return output.lower()

def main():
    word = ""
    while word != "done":
        word = input("Input a word: ").lower()
        print(word)
        if word != "done":
            print(convertToPigLatin(word))
            print(reverse(word))
            print(ROT13(word))
            print(ROT13(ROT13(word)))

main()
