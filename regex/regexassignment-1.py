#Karl Schaller
#CIS 1051 - 002 Python
#Lab #9 - Regex

import re

def part1():
    words = []
    data = open('words.txt', 'r')
    for line in data:
        words.append(line.strip())

    print("\nPART 1 ----------------------------------------------------------")
    catdog(words)
    fourLetters(words)
    hun(words)
    ingVsIon(words)
    qNoU(words)
    noVowels(words)
    onlyVowels(words)
    nt(words)
    doubleVowels(words)
    twoVowels(words)

def catdog(words):
    catdogRegex = re.compile(r'(cat)|(dog)', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if catdogRegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, 'words that contain cat or dog')

def fourLetters(words):
    fourLetterRegex = re.compile(r'^\w{4}$', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if fourLetterRegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, 'four letter words')

def hun(words):
    hunRegex = re.compile(r'hun', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if hunRegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, 'words that contain \'hun\'')

def ingVsIon(words):
    ingRegex = re.compile(r'ing$', flags = re.IGNORECASE)
    ingCount = 0
    ionRegex = re.compile(r'ion$', flags = re.IGNORECASE)
    ionCount = 0
    for word in words:
        if ingRegex.search(word):
            ingCount = ingCount + 1
            #print(word)
        elif ionRegex.search(word):
            ionCount = ionCount + 1
            #print(word)
    print('There are', ingCount, 'words that end in \'ing\'')
    print('There are', ionCount, 'words that end in \'ion\'')
    if ingCount > ionCount:
        print('More words end in \'ing\'')
    elif ionCount > ingCount:
        print('More words end in \'ion\'')
    else:
        print('Just as many words end in \'ing\' as \'ion\'')

def qNoU(words):
    qNoURegex = re.compile(r'q(?!u)', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if qNoURegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, "words that contain a 'q' not immediately " +
          "followed by a 'u'")

def noVowels(words):
    noVowelsRegex = re.compile('^[^aeiou]+$', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if noVowelsRegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, 'words that have no vowels')

def onlyVowels(words):
    onlyVowelsRegex = re.compile('^[aeiou]+$', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if onlyVowelsRegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, 'words that have only vowels')

def nt(words):
    ntRegex = re.compile("'nt$", flags = re.IGNORECASE)
    count = 0
    for word in words:
        if ntRegex.search(word):
            count = count + 1
            #print(word)
    print("There are", count, "words that end with ''nt'")

def doubleVowels(words):
    doubleVowelsRegex = re.compile('[aeiou]{2,}', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if doubleVowelsRegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, 'words that have two vowels in a row')

def twoVowels(words):
    doubleVowelsRegex = re.compile('[aeiou]\w*[aeiou]', flags = re.IGNORECASE)
    count = 0
    for word in words:
        if doubleVowelsRegex.search(word):
            count = count + 1
            #print(word)
    print('There are', count, 'words that have two vowels')

def part2():
    print("\nPART 2 ----------------------------------------------------------")

    # .* is GREEDY (it will match as much text as possible)
    # in this case it will match everything
    # .*? is NON-GREEDY or MINIMAL (it will match as few characters as possible)
    # in this case it will match nothing
    
    names = ["Satoshi Nakamoto", "Alice Nakamoto", "RoboCop Nakamoto",
             "satoshi Nakamoto", "Mr. Nakamoto", "Nakamoto", "Satoshi nakamoto"]
    nakamoto(names)

    print()
    strings = ["twenty", "twenty-one", "thirty", "thirty-two", "sixty-six",
               "eighty-three", "ninety-nine", "thirsty", "thirsty-hungry"]
    twentyTo99(strings)

    print()
    strings = ['$100.00', '$10,000.00', '$1234', '$5000.00', '$1,000,000',
               '$1234.567', '$50,00.00', '$1234,567', '$1,234.567', '1234',
               '#1234']
    dollar(strings)

def nakamoto(names):
    nakamotoRegex = re.compile('^[A-Z]\w* Nakamoto$')
    for name in names:
        print(name, end = "")
        if nakamotoRegex.search(name):
            print(" IS a Nakamoto")
        else:
            print(" IS NOT a Nakamoto")

def twentyTo99(strings):
    twentyTo99Regex = re.compile("^(twenty|thirty|fourty|fifty|sixty|seventy|" +
                                 "eighty|ninety)(-(one|two|three|four|five|" +
                                 "six|seven|eight|nine))?$")
    for string in strings:
        print(string, end = "")
        if twentyTo99Regex.search(string):
            print(" IS twenty to ninety-nine")
        else:
            print(" IS NOT twenty to ninety-nine")

def dollar(strings):
    dollarRegex = re.compile("^\$\d{1,3}((,\d{3})*|\d*)(\.\d{2})?$")
    for string in strings:
        print(string, end = "")
        if dollarRegex.search(string):
            print(" IS a dollar value")
        else:
            print(" IS NOT a dollar value")

def part3():
    print("\nPART 3 ----------------------------------------------------------")

    passwords = ['abc', 'ABC', '123', 'abcdefgh', 'abcdEFGH', '12345678',
                 'abcd1234', 'ABCD1234', 'abCD1234', 'abCDef123456',
                 'a#B#c$1#2#3']
    passwordStrength(passwords)

def passwordStrength(passwords):
    upperRegex = re.compile("[A-Z]")
    lowerRegex = re.compile("[a-z]")
    digitRegex = re.compile("\d")
    for password in passwords:
        if len(password) >= 8 and upperRegex.search(password) and \
           lowerRegex.search(password) and digitRegex.search(password):
            print(password + " is strong")
        else:
            print(password + " is not strong:")
            if len(password) < 8:
                print("Passwords must be at least eight characters long")
            if not upperRegex.search(password):
                print("Passwords must contain at least one uppercase character")
            if not lowerRegex.search(password):
                print("Passwords must contain at least one lowercase character")
            if not digitRegex.search(password):
                print("Passwords must contain at least one digit")
            

def part4():
    words = []
    data = open('words.txt', 'r')
    for line in data:
        words.append(line.strip())

    print("\nPART 4 ----------------------------------------------------------")
    
    for i in range(4):
        print(passwordGenerator(words))

def passwordGenerator(words):
    import random
    
    password = []
    while len(password) < 4:
        word = words[random.randint(0, len(words))]
        if len(word) >= 4:
            password.append(word.lower())

    return "".join(password)        

if __name__ == '__main__':
    part1()
    part2()
    part3()
    part4()
    
