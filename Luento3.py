raha = float(input("Kuinka paljon sinulla on rahaa?"))

if raha >= 5:
    print("Voit ostaa kahvin!")

if raha < 5:
    print("Oi voi, sinulla ei ole riittävästi rahaa.")

print("Kiitos ja hei!\n")

pituus = int(input("Kuinka pitkä olet?\n"))

if 170 <= pituus < 180:
    print("Oletpa pitkä!\n")

koira = input("Mikä on koiran nimi?").lower()
kissa = input("Mikä on kissan nimi?").lower()
# .lower komento muuttaa kaikki kirjaimet pieniksi, vaikka kirjoittaisi IsoJa Kirjaimia

if koira == kissa:
    print("Oho, niillä on sama nimi!\n")

koira = input("Mikä on koiran nimi?").lower()
if koira == "musti":
    print("Oho, niillä on sama nimi!\n")
#Tässä verrattiin merkkijonoa eikä noita muuttujia kissa ja koira.

a = True
b = False

if a and b:
    print("molemmat on totta!")

if a or b:
    print("Toinen tai molemmat on totta.")

if not a and b:
    print("Kumpikaan ei ole totta.\n")


raha = float(input("Kuinka paljon sinulla on rahaa?"))

if raha >= 5:
    print("Voit ostaa kahvin!")

else:
    print("Oi voi, sinulla ei ole riittävästi rahaa.\n")
