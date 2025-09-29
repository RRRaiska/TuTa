# Kirjoita peli, jossa tietokone arpoo kokonaisluvun väliltä 1..10.
# Kone arvuuttelee lukua pelaajalta siihen asti, kunnes tämä arvaa oikein.
# Kunkin arvauksen jälkeen ohjelma tulostaa tekstin Liian suuri arvaus, Liian pieni arvaus tai Oikein.
# Huomaa, että tietokone ei saa vaihtaa lukuaan arvauskertojen välissä.
import random

luku = int(input("Arvon luvun 1 ja 10 väliltä. Arvaa minkä luvun arvon: "))
luku <= 1 and luku >= 10

while (luku <=1 or luku >=10):

    print("Liian suuri arvaus.")
    print("Liian pieni arvaus.")
    print("Oikein!")

# Mistähän johtuu että import random ei toimi. se menee harmaaksi ja sanoo että unused import statement 'import random'.
# se kuitenkin toimii tuolla mun luento 4 tehtävissä.

