# Write your solution here
number1 = int(input("Please type in the number: "))
number2 = int(input("Please type in another number: "))

if number1 > number2:
    print(f"The greatest number was {number1}")
    
elif number1 < number2:
    print(f"The greatest number was {number2}")

elif number1 == number2:
    print("The numbers are equal")