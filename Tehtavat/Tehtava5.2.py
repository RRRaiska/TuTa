# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka,
# kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.
# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää
# antamalla sort-metodille argumentiksi reverse=True.


lista =[]

lukuja = input("Anna luku? \nKun haluat lopettaa lukujen antamisen paina Enter. ")

while lukuja != "":
    lukuja = int(lukuja)
    lista.append(lukuja)
    lukuja = input("Anna luku? Kun haluat lopettaa lukujen antamisen paina Enter. ")

lista.sort(reverse=True)
print(lista[0:5])
