nimi = input("Kerro etunimesi: ")
snimi = input("Kerro sukunimesi: ")
print("Tervehdys ", nimi, snimi, "ja hyvää iltaa!")

print(nimi)

#Tämä on kommentti

eka = -9
toka = 12_456_123_180
kolmas = 7.28
neljas = 3-2j

print(eka, toka, kolmas, neljas)

name = "Raisa"
age = 45

print("Tervehdys,", name, age, "vuotta.")

print("terve, " + name + " " + str(age) + " vuotta.")
#näyttää kamalalta tuo ylempi

print("terve,", name,str(age), " vuotta.")
#näyttää paremmalta pilkuilla!

name = input("Anna nimesi: ")
age = int(input("Anna ikäsi: "))

print("Tervehdys,", name, age, "vuotta.")

#miten muutetaan muuttujia, kysytään tekstinä ikä ja muutetaan se seuraavalla rivillä kokonaisluvuksi.
ika_str = input("Kuinka vanha olet? ")
ika = int(ika_str)

#Tässä esimerkissä ei pysty laittamaan pistettä oikeaan kohtaan, koska ollaan juuri muutettu tuota ikää str:stä int:tiin.
print("Ai, olet syntynyt vuonna", 2025-ika, ".")


#Muotoilu aloitetaan f-kirjaimella ennen lainausmerkkejä.
print(f"Ai, olet syntynyt vuonna {2025-ika}.")

#.5f näyttää 5 desimaalin tarkkuudella
pituus = int(input("Anna pituutesi kokonaislukuna: "))
paino = float(input("Anna painosi: "))

#Muuttuja jossa lasku suoritetaan
bmi = paino / (pituus / 100) ** 2

print("Pituus-paino-indeksisi on", bmi)
#aaltosulkeissa ennen pistettä (desimaaleja) voi laittaa siihen tyhjiä merkkejä ihan numerona. Esim. {bmi:10.2f} antaa luvun (4 kpl) ja sen eteen välilyöntejä (6) niin paljon kuin on tuohon lukuun laitettu.
print(f"Pituus-paino-indeksisi on {bmi:.2f}")
print(f"Pituus-paino-indeksisi on {bmi:10.2f}")


#kotitehtävissä tarvitaan matikkakirjastoa

