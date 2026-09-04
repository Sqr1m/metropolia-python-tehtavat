ikä = int(input("Anna ikä: "))
laji = input("Anna laji: ")

print("Voit tilata:")
print("kahvia")

if laji == "ihminen" and ikä >= 18:
    print("viiniä")

if laji == "tonttu" and ikä >= 100:
    print("olutta")

if laji == "robotti":
    print("öljyä")