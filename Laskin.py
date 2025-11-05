#Yhteenlasku
def summa(num1, num2):
    print("Yhteenlaskun tulos on: ", num1+num2)
    return

#vähennyslasku
def vahennys(num1, num2):
    print("Vähennyslaskun tulos on: ", num1-num2)
    return

#kertolasku
def kerto(num1, num2):
    print("Kertolaskun tulos on: ", num1*num2)
    return

#jakolasku
def jako(num1, num2):
    if b != 0:
        print("Jakolaskun tulos on: ", num1/num2)
    else:
        print("Nollalla ei voi jakaa")
    return

print("-------Tervetuloa käyttämään laskinta!-------")
while True:
    print("\nValitse mitä toimintoa haluat käyttää? \n A: Yhteenlasku \n B: Vähennyslasku"
          "\n C: Kertolasku \n D: Jakolasku ")
    valinta = input("Valintasi (A - D), Q lopettaa: ").upper()

    #while loopin katkaisu
    if valinta == "Q":
        print("Ohjelma lopetetaan, kiitos hei!")
        break

    #Lukuja voi sekoittaa keskenään, mutta lukuja ja merkkijoukkoa ei voi ilman, että sen castaa.
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        summa(a,b)
        # print("Yhteenlasku:", a + b)
    elif valinta == "B":
        vahennys(a,b)
        #print("Vähennyslasku:", a - b)
    elif valinta == "C":
        kerto(a,b)
        #print("Kertolasku:", a * b)
    elif valinta == "D":
        jako(a,b)
        #print("Desimaalijakolasku", a / b)
    else:
        print("Valitasi on virheellinen.")

