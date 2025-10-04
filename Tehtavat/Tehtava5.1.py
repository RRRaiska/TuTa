# Kirjoita ohjelma, joka kysyy käyttäjältä arpakuutioiden lukumäärän.
# Ohjelma heittää kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan.
# Käytä for-toistorakennetta.

import random

nopat = int(input("Montaako noppaa haluat minun heittävän? "))

luvut = random.randint (1,6)
luvut = []
luvut.append(nopat)

print(f"Nopien silmälukujen summa on {nopat} * {luvut}")