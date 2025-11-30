money = float(input("Enter the amount of money you have: "))

if money >= 5:
    print("You can buy a coffee.")

height =int(input("How tall are you? "))

if 170 <= height < 180:
    print("You are tall!")

a = True
b = False

if a & b:
    print("Both are true")
if a | b:
    print("Either of them, or both, is true")
if not a & b:
    print("Neither are true")

number = int(input("Please, type a number: "))

if number < 0:
    print("The number is negative.")
else:
    print("The number is positive.")

age = int(input("Enter your age: "))

if age >= 65:
    print("You are retired.")
elif age >= 18:
    print("You are working age.")
elif age >= 7:
    print("You are in school.")
else:
    print("You are a small child.")

number_other = int(input("Please type another number: "))
if number_other > 0:
    if number_other % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
else:
    print("The number is negative or zero.")

number_third = int(input("Please type a 3rd number: "))
if number_third > 0 and number_third % 2 == 0:
    print("The 3rd number is even.")
elif number_third > 0 and number_third % 2 != 0:
    print("The 3rd number is odd.")
else:
    print("The 3rd number is negative or zero.")