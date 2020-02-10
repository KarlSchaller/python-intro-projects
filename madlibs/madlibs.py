import re

libFile = open("madlib1.txt", 'r')
outFile = open('out.txt', 'w')
madRegex = re.compile(r"(NOUN|ADJECTIVE|VERB|ADVERB)")
output = ""

for line in libFile:
    line = line.strip()
    match = madRegex.search(line)
    while match:
        print("Please enter a " + match.group())
        word = input()
        output = madRegex.sub(word, line, 1)
        match = madRegex.search(line)
    output = output + line + "\n"
    outFile.write(line+"\n")

print(output)
outFile.close()
