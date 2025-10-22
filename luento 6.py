# Funktiomäärittelyt
# parametrit laitetaan funktion sulkeisiin
def terve(tervehdys,kerrat):
    #Funktion nimi kannattaa olla myös kuvaava kuten muuttujillakin
    for k in range(kerrat):
        print(tervehdys)
    return

def yhteenlasku(num1, num2, num3):
    _summa = num1+num2+num3
    return _summa

#pääohjelma, jossa kutsutaan myös funktioita
#print("Uusi päivä alkaa tervehdyksellä:")
#terve("Moikka", 3)
#print("Jatketaan eteenpäin!")
#terve("hei hei", 5)
#parametrit täytetään järjestyksessä. tämä ohjelma näyttää nimet parametreille kuten yltä huomaat.

luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna luku: "))
luku3 = int(input("Anna luku: "))

summa = yhteenlasku(luku1, luku2, luku3)
print("lukujen summa on ", summa)

# YRITÄ PÄIVITTÄÄ LASKIN KÄYTTÄEN FUNKTIOITA ENS KERTAA VARTEN, TEE KOTITEHTÄVÄT (PAKOLLISIA), HARJOITTELE EKSTRA-TEHTÄVIÄ. viimeinen kotitehtävä ei ole pakollinen.








