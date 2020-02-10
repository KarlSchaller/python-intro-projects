number = 22103694513205322674
print(number)
while number != 1:
    if number % 2 == 0:
        number /= 2
    elif number % 2 == 1:
        number += 1
    else:
        print(number)
    print(number)
