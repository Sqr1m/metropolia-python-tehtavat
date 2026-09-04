import random


def paluuarvonaansatunnaisen():
    return random.randint(1, 6)


if __name__ == "__main__":
    while True:
        silmaluku = paluuarvonaansatunnaisen()
        print(silmaluku)

        if silmaluku == 6:
            break
