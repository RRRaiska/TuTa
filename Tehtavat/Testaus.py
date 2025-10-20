# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
# antamalla sort-metodille argumentiksi reverse=True.

import random

#nopat = input("Montako noppaa? ")
#silmaluvut = []
#noppienHeitot = 0

#for noppienHeitot < nopat:
#for nopat in random.randint(1,6):
 #   noppienHeitot += 1
  #  silmaluvut.append(noppienHeitot)
   # print(noppienHeitot)
    #print(silmaluvut)


nopat = int(input("Anna kuutioiden määrä: "))
summa = 0
for i in range(nopat):
    print(nopat)
    heitto = random.randint(1,6)
    print("Heitto:", heitto)
    summa += heitto
    print("Summa ", summa)