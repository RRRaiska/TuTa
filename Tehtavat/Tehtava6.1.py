# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
# silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan
# kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.
import random

def satunnainen_luku():
    return random.randint(1, 6)

nopat = []
luku = 0

while nopat != 6:
    satunnainen_luku()
print(nopat)

