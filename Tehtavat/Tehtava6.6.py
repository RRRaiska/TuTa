# Kirjoita funktio, joka saa parametreinaan pyöreän pizzan halkaisijan senttimetreinä
# sekä pizzan hinnan euroina. Funktio laskee ja palauttaa pizzan yksikköhinnan
# euroina per neliömetri. Pääohjelma kysyy käyttäjältä kahden pizzan halkaisijat
# ja hinnat sekä ilmoittaa, kumpi pizza antaa paremman vastineen rahalle
# (eli kummalla on alhaisempi yksikköhinta). Yksikköhintojen laskennassa on hyödynnettävä
# kirjoitettua funktiota.
import math

def yksikkohinta(halkaisija,hinta):
    #lasketaan pinta-ala neliömetreinä
    sade = halkaisija/2
    pinta_ala = math.pi * (sade / 100) ** 2 #cm -> metreiksi
    #yksikköhinta = €/nm2
    return hinta/pinta_ala

#main programme
halkaisija1 = float(input("Halkaisija pizza1 (cm): "))
hinta1 = float(input("Hinta pizza1 (€): "))

halkaisija2 = float(input("Halkaisija pizza2 (cm): "))
hinta2 = float(input("Hinta pizza2 (€): "))

#Lasketaan yksikköhinnat
pizza1 = yksikkohinta(halkaisija1,hinta1)
pizza2 = yksikkohinta(halkaisija2,hinta2)
print(f"Pizza 1 yksikköhinta on {pizza1:.2f} €/nm2")
print(f"Pizza 2 yksikköhinta on {pizza2:.2f} €/nm2")

#Verrataan
if pizza1 < pizza2:
    print("Ensimmäinen pizza on yksikköhinnaltaan halvempi.")
elif pizza2 < pizza1:
    print("Toinen pizza on yksikköhinnaltaan halvempi.")
else:
    print("Yksikköhinta on sama molemmilla pizzoilla.")