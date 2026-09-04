
c = "admin"
d = "admin"

i = 0
while i != 5:

    a = input("käyttäjätunnus: ")
    b = input("salasana: ")

    if a == c and b == d:
        print("Tervetuloa ")
        break

    else:
        print("Pääsy evätty")
        i += 1

