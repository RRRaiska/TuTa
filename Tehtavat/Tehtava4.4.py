# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.


import random
luku = int(input("Arvon luvun 1 ja 10 väliltä. Arvaa minkä luvun arvon: "))

arpa = random.randint (1,10)

while luku == arpa:
        while luku > arpa and luku != arpa:
            print(f"Arvoin luvun {arpa}. Liian pieni arvaus.")
            luku = int(input("Arvaa uudelleen: "))
            while luku > arpa and luku != arpa:
                print(f"Arvoin luvun {arpa}. Liian suuri arvaus.")
                luku = int(input("Arvaa uudelleen: "))
print(f"Arvoin luvun {arpa}. Arvasit oikein!")

# en saanut tätä toimimaan. Enkä ymmärrä miksi. Olen kuitenkin ylpeä, että pääsin tähän asti.
# Oli ihan älytömän vaikeita tehtäviä. Tuntuu ettei ohjeissa ole riittävästi tietoa,
# eikä googlaaminen yksinään auta.