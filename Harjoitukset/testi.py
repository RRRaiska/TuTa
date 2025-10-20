import random


nopat = int(input("Montako noppaa? "))
silmaluvut = []
noppienHeitot = 0

for noppienHeitot in nopat:
    random.randint(1,6)
    noppienHeitot += 1
    silmaluvut.append(noppienHeitot)
print(silmaluvut)