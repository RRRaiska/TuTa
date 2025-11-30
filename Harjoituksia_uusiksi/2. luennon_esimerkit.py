user = input("Enter your name: ")
print("Nice to meet you, " + user + "!")

user = "Heidi"
print(user)

number1 = 100
number2 = "100"

print(number1 + number1)
print(number2 + number2)

height = 169
weight = 77.2

bmi = weight / (height / 100) ** 2
print("The bmi is",bmi)

input_str = input("How old are you? ")
age = int(input_str)
print("Oh, so you were born in", 2025-age)

age = int(input("How old are you?"))
print("Oh, so you were born in", 2025-age)

fahrenheit_str = input("Enter a temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit_str)
celsius = (fahrenheit-32)*5/9

print("The temperature in Celsius: " +str(celsius))
print(f"The temperature in Celsius: {celsius:6.2f}")

import math
print(f"{'Pi':12s}:{math.pi:10.5f}")
print(f"{'e':12s}:{math.e:10.5f}")