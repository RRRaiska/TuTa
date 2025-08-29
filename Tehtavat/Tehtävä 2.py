#kuusi tehtävää tähän kakkoseen! Älä käytä tiedoston nimessä ääkkösiä tai välilyöntejä.
#https://github.com/RRRaiska/TuTa/tree/main/Tehtavat vie tämä tehtävien mukana Omaan vastaukseen.

print("Tehtävä 2.1")
nimi = input("Mikä sinun nimesi on? ")

print("Terve", nimi+"!")


print("Tehtävä 2.2")
import math
ympSade = float(input("Kerro minulle jokin luku ympyrän säteeksi, niin lasken sinulle sen pinta-alan. Säde: "))
pintaAla = (ympSade * ympSade) * math.pi

print(f"Ympyrä, jonka säde on {ympSade} cm, niin sen pinta-ala on {pintaAla:.2f} cm2.")

print("Tehtävä 2.3")
print("Lasken sinulle suorakulmion piirin ja pinta-alan.")
kanta = int(input("Anna pitkän sivun pituus kokonaislukuna: "))
korkeus = int(input("Anna lyhyemmän sivun pituus myös kokonaislukuna: "))

piiri = (kanta + korkeus) * 2
pintaAla2 = kanta * korkeus

print(f"Suorakulmion piiri on {piiri} cm ja sen pinta-ala on {pintaAla2} cm2. ")

print("Tehtävä 2.4")
print("Pyydän sinulta 3 kokonaislukua.")
luku1 = int(input("Haluamasi luku 1 on: "))
luku2 = int(input("Haluamasi luku 2 on: "))
luku3 = int(input("Haluamasi luku 3 on: "))

summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiArvo = summa / 3

print(f"Antamiesi lukujen summa on {summa}, tulo on {tulo} ja keskiarvo on {keskiArvo}. ")

print("Tehtävä 2.5")

print("Muutan sinulle vanhoja massan mittoja: leiviskä, naula ja luoti kokonaisiksi kilogrammoiksi ja grammoiksi.")
leiviska = float(input("Leiviskät: "))
naula = float(input("Naulat: "))
luoti = float(input("Luodit: "))

luoti = 13.3
naula = 32 * luoti
leiviska = 20 * naula

summa2 = (leiviska + naula + luoti) / 1000
print(f"Antamasi massat nykymittojen mukaan on {summa2}. kg")