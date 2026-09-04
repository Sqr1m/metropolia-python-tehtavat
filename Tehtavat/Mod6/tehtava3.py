while True:
    a = int(input("Anna kokonaisluku: "))

    if a < 2:
        print(f"{a} ei ole alkuluku")
    else:
        for i in range(2, a):
            if a % i == 0:
                print(f"{a} ei ole alkuluku")
                break
        else:
            print(f"{a} on alkuluku")
