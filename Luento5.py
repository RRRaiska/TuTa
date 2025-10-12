# esimerkki 1

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]

names = ["Pertti", "Matti"]

print(nimet[2])
print(nimet[-3])
print(nimet[1:3]) #: on aloituspiste. :jälkeinen luku on se mitä EI enää näytetä
print(nimet[:3])
print(nimet[1:])

print(len(nimet))
# yllä oleva on sama kuin alla oleva
maara = len(nimet)
print(maara)

#print(nimet[5]) # ei ole määritelty 5 antaa virheen.

nimilista = [] #tyhjä lista, jolle voidaan lisätä asioita.
nimi = input("Anna eka nimi tai lopeta Enterillä: ")
while nimi != "":
    nimilista.append(nimi)
    nimi = input("Anna seuraava nimi tai lopeta Enterillä: ")

print(nimilista)
#remove poistaa listalta asian joka tuplana, ja sen joka on annettu ensimmäisenä.

#nimet.remove("Pekka")
#print(nimet)

nimet.insert(3,"Teppo")
print(nimet)

nimet.extend(names)
print(nimet)

print(nimet.index("Olga")) #antaa Olgan listan sijainnin eli arvon/itemin/alkion

if "Matti" in nimet:
  print("Matti löytyy.")
else:
    print("Matti puuttuu.")

print(nimet)
nimet.sort()
print(nimet)
#sort antaa aina tekstit aakkosittain, numerot pienimmästä suurimpaan. ellei käännä järjestystä.
# sort muuttaa myös indeksipaikat.

nimet.sort(reverse=True) #kääntää järjestyksen öökkösistä tai suurimmasta alaspäin.

for koira in nimet: #koira sana voi olla mitä vaan!
    print("Tervehdys," ,koira)
print("For looppi loppui.")
# koiraksi ensin tallentuu viivi, sit palataan for loopin alkuun ja silloin koiraksi tallentuu Ahmed. jne.
# jos lista on tyhjä niin silloin tulee lopun printti For looppi loppui.
# KATSO ITSE RANGE FUNKTIO. TEE MYÖS HARJOITUKSET NIIN OPIT. TEE NÄÄ EKA.


