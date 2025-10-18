# Kirjoita ohjelma, joka tulostaa viestin "Morjens!" ja sen jälkeen kysyy
# "Jatketaanko?" niin kauan, kunnes käyttäjä syöttää "Ei".Tämän jälkeen ohjelma tulostaa
# "Ei sitten!" ja lopettaa. Katso esimerkki alta:

#Morjens!
#Jatketaanko? yes
#Morjens!
# Jatketaanko? oui
# Morjens!
# Jatketaanko? ja
# Morjens!
# Jatketaanko? Ei
# Ei sitten!

print("Morjens!")
vastaus = input("Jatketaanko? ")

while vastaus != "Ei":
    vastaus = input(" Morjens! Jatketaanko? ")
else:
    print("Ei sitten.")