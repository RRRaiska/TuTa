# Kirjoita funktio, joka saa parametrinaan listan kokonaislukuja.
# Ohjelma palauttaa toisen listan, joka on muuten samanlainen kuin
# parametrina saatu lista paitsi että siitä on karsittu pois kaikki parittomat luvut.
# Kirjoita testausta varten pääohjelma, jossa luot listan, kutsut funktiota
# ja tulostat sen jälkeen sekä alkuperäisen että karsitun listan.

def kokonaisluvut(kaikkiluvut):
    return kaikkiluvut

kaikkiluvut = []
parittomat = []

# pääohjelma
numero = int(input("Anna numero? "))
kaikkiluvut.append(numero)

while numero != "":
    kaikkiluvut.append(numero)
    numero = int(input("Anna numero? "))

if numero % 2 == 0:
    parittomat.append(numero)
    print(parittomat)

else:
    kokonaisluvut(kaikkiluvut)
    kaikkiluvut.sort()

# Tässä yritykseni. Ei toiminut tämäkään. en ymmärrä yhtään mitään.

#def parilliset(l):
#   uusi_lista = []
#   for l in l:
    #if luku % 2 == 0:
    #   uusi_lista.append(luku)
    #return uusi_lista

#pääohjelma
# luvut = [5,12,3,44,8,17,0]
#luvut2 = parilliset(luvut)

#print("Alkuperäinen lista:", luvut)
#print("Parillinen lista:", luvut2)