luku = int(input("Anna jokin kokonaisluku: ",))

if luku < 0:
    print(f"Luvun itseisarvo on {luku * -1}.")

else:
    print(f"Luvun itseisarvo on {luku}.\n")


#Oikea vastaus oli:
nimi = input("mikä on nimesi? ").lower()

if nimi != "Matti":
    annokset = int(input("Montako keittoannosta? "))
    print(f"Kokonaishinta on {annokset * 5.9}")
    print("Seuraava, kiitos!")

else:
    print("Seuraava, kiitos!")


ika = int(input("Anna ikäsi: "))

if ika >= 65:
    print("olet eläkeiässä.")
elif ika >= 18:
    print("olet työikäinen.")
elif ika >= 7:
    print("olet kouluikäinen.")
else:
    print("olet pikkulapsi.")

n = int(input("Anna kokonaisluku: "))

if n > 0:
    if n % 2 == 0:
        print("Numero on parillinen.")
    else:
        print("Numero on pariton.")
else:
    print("Numero on negatiivinen tai nolla.")