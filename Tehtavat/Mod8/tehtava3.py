a = str(
    input(
        "Haluatko: syottaa uuden lentoaseman,  hakea jo syötetyn lentoaseman tiedot"
        "vai lopettaa? (syötä 'uusi' tai 'hakea' tai 'lopeta'): "
    )
)

info = {}
while a != "lopeta":
    if a == "uusi":
        b = str(input("Anna ICAO code: "))
        c = str(input("Anna lentoaseman nimi: "))
        info[b] = c
    elif a == "hakea":
        d = str(input("Anna ICAO code: "))
        print(info[d])

    a = str(
        input(
            "Haluatko: syottaa uuden lentoaseman,  hakea jo syötetyn lentoaseman tiedot"
            "vai lopettaa? (syötä 'uusi' tai 'hakea' tai 'lopeta'): "
        )
    )
