import random

b = 0

for i in range(int(input("Anna arpakuutioiden lukumäärän: "))):
    b += random.randint(1, 6)

print(f"Tulos {b}")