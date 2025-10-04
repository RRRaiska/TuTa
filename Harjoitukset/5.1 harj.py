# Luo ohjelma, joka kysyy käyttäjältä hänen lempivärinsä. Tarkista, löytyykö lempiväri ennalta
# määritellystä värilistasta, ja vastaa sen mukaisesti. Määrittele lista itse.

lempivari = input("Mikä on lempivärisi? ")
varit = ["sininen", "punainen", "keltainen", "vihreä", "valkoinen", "musta"]

if lempivari in varit:
    print("Lempivärisi" ,lempivari, "on listalla.")
else:
    print("Lempivärisi" , lempivari, "ei ole listalta.")