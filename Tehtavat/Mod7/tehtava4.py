def list_kokonaisluvut(lista):
    a = 0
    for i in lista:
        a += i
    return a


def main():
    lista = [1, 2, 3, 4, 10]
    print(list_kokonaisluvut(lista))


if __name__ == "__main__":
    main()
