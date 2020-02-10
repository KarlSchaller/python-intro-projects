import re

# . wildcard character
# .+ plus means at least one
# \s anything that is white space \S anything that is not white space
# \w letter, digit, or underscore \W anything that is not

snnRegex = re.compile(r"\d\d\d-\d\d}-\d\d\d\d") # digits
snnRegex = re.compile(r"\d{3}-\d{2}-\d{4}") # same as previous line
match = snnRegex.search("My SSN is 111-11-1112")
print(match)
print(match.group())
print(match.groups())
print(snnRegex.findall("My SSN is 111-11-1112 111-12-2212"))

batRegex = re.compile(r'Batman|Tina Fey') # | is an 'or'
print(batRegex.search("Na na na na na na na na na Batman!"))
print(batRegex.search("Na na na na na na na na na Tina Fey!"))
batRegex = re.compile(r'Bat(wo)?man') # ()? is optional
print(batRegex.search("Batman the animated series"))
print(batRegex.search("Batwoman the animated series"))
batRegex = re.compile(r'Bat(wo)*man') # ()* is optional infinite number of times
print(batRegex.search("Batwowowowowowowowoman"))
jokerRegex = re.compile(r'(Ha){3,5}$', re.I) #{a,b} a to b instances $ no more
print(jokerRegex.search("HaHa"))
print(jokerRegex.search("HaHaHaHaHa"))
print(jokerRegex.search("haHAHAhaHAHaH"))

phoneRegex = re.compile(r"(\()?\d{3}(\))?(-| )?\d{3}(-| )?\d{4}")
print(phoneRegex.search("my number is 1111111111"))
print(phoneRegex.search("my number is 111-111-1111"))
print(phoneRegex.search("my number is (111) 111 1111"))

doubleVowel = re.compile(r"[aeiou]{2}")
print(doubleVowel.search("needs"))
print(doubleVowel.search("thorough"))
