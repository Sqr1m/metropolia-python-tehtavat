def averages(a):
    b = 0

    for c in a:
        b += c

    return b / len(a)


def main():
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))
    c = float(input("Anna kolmas luku: "))
    d = float(input("Anna neljäs luku: "))

    a = [a, b, c, d]

    print(f"{averages(a):.2f}")


if __name__ == "__main__":
    main()
