# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

nopat = int(input("Anna kuutioiden määrä: "))
summa = 0
for i in range(nopat):
    print(nopat)
    heitto = random.randint(1,6)
    print("Heitto:", heitto)
    summa += heitto
    print("Summa ", summa)