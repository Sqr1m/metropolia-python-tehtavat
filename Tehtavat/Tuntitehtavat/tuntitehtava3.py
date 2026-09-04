while True:
    a = int(input("Anna vuosi: "))

    if a < 1896:
        break

    if (a % 4 == 0 and a != 2020 or a == 2021):
        print("Se on olympiavuosi")
    else:
        print("Ei ollut olympiavuosi")