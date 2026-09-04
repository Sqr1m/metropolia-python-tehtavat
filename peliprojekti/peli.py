import sys

nimi = input("Nimi: ")
ika = int(input("Ikä: "))

if ika < 12:
    print("Olet alaikäinen.")
    sys.exit()

print(f"Tervetuloa, {nimi}!")

while True:
    print()
    print("Päävalikko")
    print("1 - Tulosta tervehdys")
    print("2 - Tulosta satunnainen viesti")
    print("3 - Tulosta pelaajan nimi")
    print("lopeta - Lopeta peli")

    komento = input("Anna komento: ")

    if komento == "1":
        print("Hei! Hauskaa peliä.")

    elif komento == "2":
        print("Aurinko paistaa tänään.")

    elif komento == "3":
        print(f"Pelaajan nimi on {nimi}.")

    elif komento == "lopeta":
        print("Kiitos pelaamisesta!")
        break

    else:
        print("Tuntematon komento.")