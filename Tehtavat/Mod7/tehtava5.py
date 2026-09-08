def list_kokonaisluvut(lista):
    toinen_lista = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            toinen_lista.append(lista[i])
    return toinen_lista


if __name__ == "__main__":
    lista = [1, 3, 3, 4, 10]
    print(lista)
    print(list_kokonaisluvut(lista))
