#Karl Schaller
#CIS 1051 - 002 Python
#Lab #7 - Hawaiian Word Pronouncer

def inputWord():
    word = ""
    badChars = "a"
    while badChars != "":
        badChars = ""
        word = input("Enter a Hawaiian word => ").lower()
        for letter in word:
            if letter not in "aeioupkhlmnw '":
                badChars = badChars + "'" + letter + "'" + " "
        if badChars != "":
            print(badChars + "are not valid characters in a Hawaiian word")
    return word

def pronunciation(word):
    pronunciation = ""
    i = 0
    while i < len(word):
        #if letter is 'A'
        if word[i] == "a":
            if i+1 < len(word):
lu                if word[i+1] == "i" or word[i+1] == "e":
                    pronunciation += "eye"
                    i += 1
                elif word[i+1] == "o" or word[i+1] == "u":
                    pronunciation += "ow"
                    i += 1
                else:
                    pronunciation += "ah"
                if not (i >= len(word)-1 or word[i+1] == " " or word[i+1] == "'"):
                    pronunciation += "-"
            else:
                pronunciation += "ah"

        #if letter is 'E'
        elif word[i] == "e":
            if i+1 < len(word):
                if word[i+1] == "i":
                    pronunciation += "ay"
                    i += 1
                elif word[i+1] == "u":
                    pronunciation += "eh-oo"
                    i += 1
                else:
                    pronunciation += "eh"
                if not (i >= len(word)-1 or word[i+1] == " " or word[i+1] == "'"):
                    pronunciation += "-"
            else:
                pronunciation += "eh"

        #if letter is 'I'
        elif word[i] == "i":
            if i+1 < len(word):
                if word[i+1] == "u":
                    pronunciation += "ew"
                    i += 1
                else:
                    pronunciation += "ee"
                if not (i >= len(word)-1 or word[i+1] == " " or word[i+1] == "'"):
                    pronunciation += "-"
            else:
                pronunciation += "ee"

        #if letter is 'O'
        elif word[i] == "o":
            if i+1 < len(word):
                if word[i+1] == "i":
                    pronunciation += "oyo"
                    i += 1
                elif word[i+1] == "u":
                    pronunciation += "ow"
                    i += 1
                else:
                    pronunciation += "oh"
                if not (i >= len(word)-1 or word[i+1] == " " or word[i+1] == "'"):
                    pronunciation += "-"
            else:
                pronunciation += "oh"

        #if letter is 'U'
        elif word[i] == "u":
            if i+1 < len(word):
                if word[i+1] == "i":
                    pronunciation += "ooey"
                    i += 1
                else:
                    pronunciation += "oo"
                if not (i >= len(word)-1 or word[i+1] == " " or word[i+1] == "'"):
                    pronunciation += "-"
            else:
                pronunciation += "oo"

        #consonants
        elif word[i] == "w":
            if i != 0:
                if word[i-1] == "i" or word[i-1] == "e":
                    pronunciation += "v"
                else:
                    pronunciation += "w"
            else:
                pronunciation += "w"
        else:
            pronunciation += word[i]
        i += 1
            
    return pronunciation

def replay():
    response = "a"
    while not (response.upper() == "Y" or response.upper() == "YES" or response.upper() == "N" or response.upper() == "NO"):
        response = input("Do you want to enter another word? Y/YES/N/NO ==> ")
        if response.upper() == "Y" or response.upper() == "YES":
            return True
        elif response.upper() == "N" or response.upper() == "NO":
            return False
        else:
            print("Enter Y, YES, N, or NO")
            
if __name__ == "__main__":
    playing = True
    while playing == True:
        word = inputWord()
        print(word.upper() + " is pronounced " + pronunciation(word).capitalize())
        playing = replay()
