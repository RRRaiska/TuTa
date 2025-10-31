# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa listassa olevien lukujen summan.
# Kirjoita testausta varten pääohjelma, jossa luot listan,
# kutsut funktiota ja tulostat sen palauttaman summan.

def kokonaisluvut_yhteen(luku1, luku2, luku3):
    summa = luku1+luku2+luku3
    return summa

lista =[]
luku1 = int(input("Anna kokonaisluku: "))
luku2 = int(input("Anna kokonaisluku: "))
luku3 = int(input("Anna kokonaisluku: "))

lista.append(luku1)
lista.append(luku2)
lista.append(luku3)

summa = kokonaisluvut_yhteen(luku1,luku2,luku3)
print(lista)
print("Lukujen summa on",summa,".")
