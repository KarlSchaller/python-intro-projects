#Karl Schaller
#CIS 1051 - 002 Python
#Lab #9 - Brute-Force PDF Password Breaker

import PyPDF2

reader = PyPDF2.PdfFileReader(open('encrypted.pdf', 'rb'))
print(reader.isEncrypted)
#print(reader.getPage(0))
                              
dictionary = open("dictionary.txt", 'r').readlines()
password = "PASSWORD NOT CRACKED"

for word in dictionary:
    word = word.strip()
    #print(word)
    if reader.decrypt(word):
        password = word
        break        
    if reader.decrypt(word.lower()):
        password = word.lower()
        break

print('Done loop')
print(password)            
print(reader.isEncrypted)
