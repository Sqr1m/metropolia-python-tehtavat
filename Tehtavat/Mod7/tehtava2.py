import random


def paluuarvonaansatunnaisen(a):
    return random.randint(1, a)


if __name__ == "__main__":
    a = int(input("Anna nopan tahkojen määrä: "))

    while True:
        if paluuarvonaansatunnaisen(a) == a:
            break
