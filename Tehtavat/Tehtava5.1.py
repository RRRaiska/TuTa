# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

lista =[]

lukuja = input("Anna luku? \nKun haluat lopettaa lukujen antamisen paina Enter. ")

while lukuja != "":
    lukuja = int(lukuja)
    lista.append(int(lukuja))
    lukuja = input("Anna luku? Kun haluat lopettaa lukujen antamisen paina Enter. ")

lista.sort(reverse=True)
print(lista[0:5])