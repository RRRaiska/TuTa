def terve(tervehdys,kerrat):
    #Funktion nimi kannattaa olla myös kuvaava kuten muuttujillakin
    for k in range(kerrat):
        print(tervehdys)
    return

def yhteenlasku(num1, num2, num3):
    _summa = num1+num2+num3
    return _summa


luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna luku: "))
luku3 = int(input("Anna luku: "))

summa = yhteenlasku(luku1, luku2, luku3)
print("lukujen summa on ", summa)