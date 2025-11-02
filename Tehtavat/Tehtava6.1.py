# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan
# silmäluvun väliltä 1..6. Kirjoita pääohjelma, joka heittää noppaa niin kauan
# kunnes tulee kuutonen. Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun.

#import random

#def satunnainen_luku():
#    return nopat

#nopat = random.randint(1, 6)
#while nopat != 6:
#    satunnainen_luku()
#    print(nopat)

#    if nopat in range(0,6):
#        satunnainen_luku()
#    print(nopat)
#else:
#    print(nopat, "Nyt tuli kuutonen.")

# Yllä yritykseni. Kysyin tekoälyltä korjaukseen apuja. En onnistunut. Mietin varmaan jotenkin liian monimutkaisesti
# koko asiaa.

import random

def satunnainen_luku():
    return random.randint(1, 6)

# Pääohjelma
nopat = 0
while nopat != 6:
    nopat = satunnainen_luku()
    print(nopat)

print("Tulostus päättyy kuutoseen.")
