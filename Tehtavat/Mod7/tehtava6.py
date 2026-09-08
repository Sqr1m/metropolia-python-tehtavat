def yksikohinnan_euroina_per_neliometri(alaa, hinta):
    sade = alaa / 2
    ala = 3.14 * sade**2 / 10000
    return hinta / ala


def main():
    a = float(input("Anna ensimmäisen pizzan halkaisija: "))
    b = float(input("Anna ensimmäisen pizzan hinta: "))
    c = yksikohinnan_euroina_per_neliometri(a, b)

    a = float(input("Anna toisen pizzan halkaisija: "))
    b = float(input("Anna toisen pizzan hinta: "))
    d = yksikohinnan_euroina_per_neliometri(a, b)

    if c < d:
        print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
    else:
        print("Toinen pizza antaa paremman vastineen rahalle.")


if __name__ == "__main__":
    main()
