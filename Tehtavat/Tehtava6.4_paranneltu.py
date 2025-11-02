# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

def kokonaisluvut_yhteen(lista):
    return sum(lista)

lista = []
luku = int(input("Anna kokonaisluku (0 lopettaa): "))

while luku != 0:
    lista.append(luku)
    luku = int(input("Anna kokonaisluku (0 lopettaa): "))

# Hyödynnetään funktion paluuarvoa
summa = kokonaisluvut_yhteen(lista)

print("\nSyötetyt luvut:", lista)
print("Lukujen summa on", summa, ".")