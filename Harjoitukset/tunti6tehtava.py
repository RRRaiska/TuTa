
def seitsemanVeljesta(lista):
    #järjestetään lista aakkosjärjestykseen
    lista.sort()

    #tulostetaan nimet listana
    print(lista)

    #Tulostetaan nimet yksitellen
    for nimi in lista:
        print(nimi)
    return

veljekset = ["tuomas", "simeoni", "juhani", "eero","aapo","timo", "lauri"]
seitsemanVeljesta(veljekset) #lisätään veljesten nimet listalle
