def nestegallonoinatolitres(nestegallon):
    return nestegallon * 3.785


if __name__ == "__main__":
    while True:
        nestegallon = float(input("Anna nestegallonien määrä: "))

        if nestegallon < 0:
            break

        print(
            f"{nestegallon} nestegallonia on {nestegallonoinatolitres(nestegallon)} litraa."
        )
