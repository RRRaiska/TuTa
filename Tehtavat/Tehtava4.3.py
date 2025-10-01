# Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi.
# Lopuksi ohjelma tulostaa saaduista luvuista pienimmän ja suurimman.

lukuja = input("Anna luku: ")
while lukuja != " ":
    print(lukuja)
    lukuja = input("Anna luku: ")

print("Toiminto lopetettu.")

# en osannut tehdä tuota saatujen lukujen pienintä ja suurinta.

# Pieni ja suuri luku täytyy alustaa
# pieni = luku
# suuri = luku

# "" välissä ei tarvi olla välilyöntiä.
# Whilen alle numero = int(lukuja)

# vertaillaan pientä ja suurta
# if pieni == luku or numero < pieni:
# pieni = numero

# if suuri == lukuja or numero > suuri:
# suuri = numero

#lukuja = input("Anna luku: ")

pieni = lukuja
suuri = lukuja

lukuja = input("Anna luku: ")
while lukuja != " ":
    numero = int(lukuja)

    if pieni == lukuja or numero < pieni:
        pieni = numero

    if suuri == lukuja or numero > suuri:
        suuri = numero

    print(lukuja)
    lukuja = input("Anna luku: ")

    print(f"Pienin luku on {pieni}.")
    print(f"Suuri luku on {suuri}.")
print("Toiminto lopetettu.")