import random
def heita():
    eka, toka = random.randint(1,6), random.randint(1,6)
    #yllä olevan voisi kirjoittaa myös kahdella rivillä
        # eka = random.randint(1,6)
        #toka = random.randint(1,6)
    return (eka, toka) #voisi olla myös ilman sulkuja

#Pääohjelma
noppa1, noppa2 =heita() # tässä puretaan nopat omikseen. jolloin niitä voidaan käyttää erillään. Tässä myös luodaan
# eka ja toka muuttujat noppa1:seen ja noppa2:seen. Eli funktio luo arvot, mutta niitä ei ole tallenenettu mihinkään.
# TÄssä funktion antamat arvot palautetaan.
print(f"Nopista tuli {noppa1} ja {noppa2}.")