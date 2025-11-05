# Luo sanakirja, joka sisältää eri hedelmien hinnat:
# Kysy käyttäjältä hedelmän nimi ja tulosta sen hinta.

hedelmienHinnat = {"Banaani":"2 €",
                   "Omena":"3 €",
                   "Kiwi":"4 €"}

hedelma = input("Minkä hedelmän hinnan haluat tietää? Banaani, Omena vai Kiwi? ")

if hedelma in hedelmienHinnat:
    print(f"Hedelmän {hedelma} hinta on {hedelmienHinnat[hedelma]}.")
else:
    print(f"{hedelma}:lle ei löydy hintaa.")
