import sys

asiat = []


def anna_asia():
    asia = input("Anna inventaarioon lisättävä esine: ")

    if asia == "":
        print("Et antanut esinettä.")
    else:
        asiat.append(asia)
        print(f"{asia} lisättiin inventaarioon.")


def tulosta_asiat():
    if len(asiat) == 0:
        print("Inventaario on tyhjä.")
    else:
        print("Inventaarion sisältö:")

        for asia in asiat:
            print(asia)


def poista_asia():
    if len(asiat) == 0:
        print("Inventaario on tyhjä.")
    else:
        asia = input("Anna poistettava esine: ")

        if asia in asiat:
            asiat.remove(asia)
            print(f"{asia} poistettiin inventaariosta.")
        else:
            print("Esinettä ei löytynyt inventaariosta.")


def tulosta_pelaajan_tiedot(nimi, ika):
    print(f"Pelaajan nimi on {nimi}.")
    print(f"Pelaajan ikä on {ika}.")
    print(f"Inventaariossa on {len(asiat)} esinettä.")


def main_menu(nimi, ika):
    while True:
        print()
        print("Päävalikko")
        print("1 - Lisää esine inventaarioon")
        print("2 - Tulosta inventaario")
        print("3 - Poista esine inventaariosta")
        print("4 - Tulosta pelaajan tiedot")
        print("lopeta - Lopeta peli")

        komento = input("Anna komento: ")

        if komento == "1":
            anna_asia()

        elif komento == "2":
            tulosta_asiat()

        elif komento == "3":
            poista_asia()

        elif komento == "4":
            tulosta_pelaajan_tiedot(nimi, ika)

        elif komento == "lopeta":
            print("Kiitos pelaamisesta!")
            break

        else:
            print("Tuntematon komento.")


def main():
    print("Tervetuloa peliin!")

    nimi = input("Nimi: ")
    ika = int(input("Ikä: "))

    if ika < 12:
        print("Olet liian nuori pelaamaan.")
        sys.exit()

    print(f"Tervetuloa, {nimi}!")

    main_menu(nimi, ika)


if __name__ == "__main__":
    main()
