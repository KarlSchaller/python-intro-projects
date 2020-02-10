if __name__ == "__main__":
    #Technique 1: open file and read line by line
    data = open("csvnotes.csv", "r")
    #print(data)
    for line in data:
        print(line.strip())

    #Technique 2: open with readlines and store in list
    lines = open("csvnotes.csv", "r").readlines()
    for line in lines:
        print(line.strip())

    # 1) file reading
    # 2) splitting a string into a list with split()

    lines = open("csvnotes.csv", "r").readlines()
    lines = lines[1:]

    #compute average of exam 1
    total = 0
    numStudents = 0
    for line in lines:
        line = line.strip()
        print(line)
        line = line.split(",")
        print(line)
        total += int(line[1])
        numStudents += 1
    print(total/numStudents)

    #writing
    data = open("csvnotes2.csv", "w")

    for line in data:
        print(line.strip())
    data.write("Hello/n")
    for line in data:
        print(line.strip())
