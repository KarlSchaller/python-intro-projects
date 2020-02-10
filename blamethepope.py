# Blame the pope
# mm/dd/yyyy
# 0123456789

date = input("Enter a date in the format MM/DD/YYYY: ")  
month = int(date[0:2])
day = int(date[3:5])
year = int(date[6:])
valid = True

if month < 1 or month > 12:
    print("Invalid date: invalid month")
    valid = False
elif month == 4 or month == 6 or month == 9 or month == 11: #30 day months
    if day < 1 or day > 30:
        print("Invalid date: 30 day month")
        valid = False
elif month != 2: #31 day months
    if day < 1 or day > 31:
        print("Invalid date: 31 day month")
        valid = False
else: #check february
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0): #not a leap year
        if day < 1 or day > 28:
            print("Invalid date: February on a normal year is 28 days")
            valid = False
    else: #is a leap year
        if day < 1 or day > 29:
            print("Invalid date: February on a leap year is 29 days")
            valid = False

if valid == True:
    print(str(date) + " is a valid date")
