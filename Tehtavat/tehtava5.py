leiviskat = float(input("Leiviskät: "))
naulat = float(input("Naulat: "))
luodit = float(input("Luodit: "))

grammat = (leiviskat * 20 * 32 + naulat * 32 + luodit) * 13.3

kilogrammat = int(grammat // 1000)
loput_grammat = round(grammat % 1000, 2)

print("Massa nykymittojen mukaan:")
print(kilogrammat, "kilogrammaa ja", loput_grammat, "grammaa.")