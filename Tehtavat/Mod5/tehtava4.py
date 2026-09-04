import random

a = random.randint(1, 10)

while True:
    b = int(input("Anna numero: "))
    if b < a:
        print("Liian pieni arvaus")
    elif b > a:
        print("Liian suuri arvaus")
    else:
        print("Oikein!")
        break