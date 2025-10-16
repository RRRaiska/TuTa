# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
# antamalla sort-metodille argumentiksi reverse=True.
import random

lista =[]

lukuja = input("Anna luku? \nKun haluat lopettaa lukujen antamisen paina Enter. ")

while lukuja != "":
    lukuja = int(lukuja)
    lista.append(int(lukuja))
    lukuja = input("Anna luku? Kun haluat lopettaa lukujen antamisen paina Enter. ")

lista.sort(reverse=True)
print(lista[0:5])

#maara = int(input("Anna kuutioiden määrä: "))
#summa = 0
#for i in range(maara):
#    print(maara)
#    heitto = random.randint(1,6)
#    print("Heitto:", heitto)
#    summa += heitto
#    print("Summa ", summa)