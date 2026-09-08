a = str(input("Anna nimi: "))
b = set()

while a != "":
    if a not in b:
        print("Uusi nimi")
        b.add(a)
    else:
        print("Aiemmin syötetty nimi")
    a = str(input("Anna nimi: "))

print("Kaikki nimet:")
for i in b:
    print(i)
