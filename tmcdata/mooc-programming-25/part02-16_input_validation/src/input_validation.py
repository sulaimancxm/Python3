from math import sqrt

while True:
    number = int(input("Please type in a number: "))
    if number < 0:
        print("Invalid number")
    if number > 0:
        print(sqrt(number))
    if number == 0:
        break
print("Exiting...")
