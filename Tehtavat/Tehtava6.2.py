# Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen
# yhteismäärän. Muokatun funktion avulla voit heitellä esimerkiksi 21-tahkoista roolipelinoppaa.
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa
# kunnes saadaan nopan maksimisilmäluku, joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def satunnainen_luku(tahkot):

    return random.randint(1, 21)

# Pääohjelma
tahkot = int(input("Anna maksimisilmäluku: "))

nopat = 0
while nopat != tahkot:
    nopat = satunnainen_luku(tahkot)
    nopat += tahkot
    print(nopat)

print("Tulostus päättyy kuutoseen.")

#Oikea vastaus:
#def noppa(suurin):
    #return
#suurin = int(input("Kuinka suurta noppaa haluat heittää? "))
#silmaluku = 0

#while silmaluku != suurin:
    #silmaluku =noppa(suurin)
    #print("Heiton tulos:", silmaluku)