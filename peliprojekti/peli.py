import json
import os
import random


class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"{self.name} ({self.weight} kg)"


class Room:
    def __init__(self, name, item, challenge_text, correct_answer):
        self.name = name
        self.item = item
        self.challenge_text = challenge_text
        self.correct_answer = str(correct_answer)
        self.solved = False

    def show_information(self):
        print(f"\nNykyinen huone: {self.name}")

        if self.item is None:
            print("Tämän huoneen esine on jo kerätty.")
        elif self.solved:
            print(f"Haaste on ratkaistu. Voit kerätä esineen: {self.item.name}")
        else:
            print("Huoneessa on esine, mutta se on lukittu haasteeseen.")

    def solve_challenge(self):
        if self.solved:
            print("Olet jo ratkaissut tämän haasteen.")
            return

        print("\nRatkaise seuraavan algoritmin tulos:")
        print(self.challenge_text)

        answer = input("Anna algoritmin tulos: ").strip()

        if answer == self.correct_answer:
            self.solved = True
            print("Oikea vastaus! Esineen voi nyt kerätä.")
        else:
            print("Väärä vastaus. Yritä uudelleen.")

    def give_item(self):
        item_to_give = self.item
        self.item = None
        return item_to_give


class Player:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.items = []
        self.location = location

    def move(self, destination):
        if destination == self.location:
            print("Olet jo tässä huoneessa.")
        else:
            self.location = destination
            print(f"Siirryit huoneeseen: {self.location.name}")

    def collect_item(self):
        if not self.location.solved:
            print("Ratkaise ensin huoneen haaste.")
            return

        if self.location.item is None:
            print("Tässä huoneessa ei ole enää kerättävää esinettä.")
            return

        item = self.location.give_item()
        self.items.append(item)

        print(f"Keräsit esineen: {item.name}")

    def print_inventory(self):
        if len(self.items) == 0:
            print("Inventaario on tyhjä.")
        else:
            print("Inventaarion sisältö:")

            for item in self.items:
                print(f"- {item}")

    def remove_item(self):
        if len(self.items) == 0:
            print("Inventaario on tyhjä.")
            return

        item_name = input("Anna poistettava esine: ").strip()

        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                print(f"{item.name} poistettiin inventaariosta.")
                return

        print("Esinettä ei löytynyt inventaariosta.")

    def print_information(self):
        print(f"Pelaajan nimi on {self.name}.")
        print(f"Pelaajan ikä on {self.age}.")
        print(f"Pelaaja on huoneessa: {self.location.name}.")
        print(f"Inventaariossa on {len(self.items)} esinettä.")


class Menu:
    def __init__(self, player, rooms, saves, save_code):
        self.player = player
        self.rooms = rooms
        self.saves = saves
        self.save_code = save_code

    def choose_room(self):
        print("\nHuoneet:")

        for number, room in enumerate(self.rooms, start=1):
            print(f"{number} - {room.name}")

        choice = input("Valitse huoneen numero: ")

        if not choice.isdigit():
            print("Anna huoneen numero.")
            return

        room_index = int(choice) - 1

        if 0 <= room_index < len(self.rooms):
            self.player.move(self.rooms[room_index])
        else:
            print("Huonetta ei löytynyt.")

    def main_menu(self):
        while True:
            print("\nPäävalikko")
            print("1 - Näytä nykyinen huone")
            print("2 - Siirry huoneeseen")
            print("3 - Ratkaise huoneen haaste")
            print("4 - Kerää huoneen esine")
            print("5 - Tulosta inventaario")
            print("6 - Poista esine inventaariosta")
            print("7 - Tulosta pelaajan tiedot")
            print("lopeta - Lopeta peli")

            command = input("Anna komento: ").strip()

            if command == "1":
                self.player.location.show_information()

            elif command == "2":
                self.choose_room()

            elif command == "3":
                self.player.location.solve_challenge()

            elif command == "4":
                self.player.collect_item()

            elif command == "5":
                self.player.print_inventory()

            elif command == "6":
                self.player.remove_item()

            elif command == "7":
                self.player.print_information()

            elif command == "lopeta":
                if self.save_code is None:
                    self.save_code = str(random.randint(100000, 999999))

                    while self.save_code in self.saves:
                        self.save_code = str(random.randint(100000, 999999))

                self.saves[self.save_code] = {
                    "name": self.player.name,
                    "age": self.player.age,
                    "location": self.rooms.index(self.player.location),
                    "items": [item.name for item in self.player.items],
                    "rooms": [
                        {"solved": room.solved, "has_item": room.item is not None}
                        for room in self.rooms
                    ],
                }

                with open("tallennus.txt", "w", encoding="utf-8") as file:
                    json.dump(self.saves, file, ensure_ascii=False, indent=2)

                print(f"Peli tallennettu. Jatkokoodisi on: {self.save_code}")
                print("Kiitos pelaamisesta!")
                break

            else:
                print("Tuntematon komento.")


def main():
    with open("intro_ohjeet.txt", "r", encoding="utf-8") as file:
        print(file.read())

    if os.path.exists("tallennus.txt"):
        with open("tallennus.txt", "r", encoding="utf-8") as file:
            saves = json.load(file)
    else:
        saves = {}

    code = input("Anna jatkokoodi tai aloita uusi peli numerolla 2: ").strip()

    if code == "2":
        name = input("Nimi: ")
        age_text = input("Ikä: ").strip()

        if not age_text.isdigit():
            print("Ikä pitää antaa numerona.")
            return

        age = int(age_text)

        if age < 12:
            print("Olet liian nuori pelaamaan.")
            return

        print(f"Tervetuloa, {name}, peliin!")

    elif code in saves:
        print(f"Tervetuloa takaisin, {saves[code]['name']}!")

    else:
        print("Tallennusta ei löytynyt.")
        return

    excalibur = Item("Excalibur", 9999)
    mjolnir = Item("Mjolnir", 9999)

    entrance_challenge = """\
numbers = [2, 5, 1, 4]
result = 0

for number in numbers:
    if number % 2 == 0:
        result += number
    else:
        result -= 1

print(result)
"""

    boss_challenge = """\
numbers = [3, 1, 4, 1, 5]
total = 0

for number in numbers:
    if number > 2:
        total += number
    else:
        total -= number

print(total)
"""

    room_1 = Room(
        "1 (Entrance)",
        excalibur,
        entrance_challenge,
        4,
    )

    room_2 = Room(
        "2 (First Boss)",
        mjolnir,
        boss_challenge,
        10,
    )

    rooms = [room_1, room_2]

    if code == "2":
        player = Player(name, age, room_1)
        save_code = None

    else:
        saved = saves[code]

        player = Player(saved["name"], saved["age"], rooms[saved["location"]])

        available_items = {"Excalibur": excalibur, "Mjolnir": mjolnir}

        for item_name in saved["items"]:
            player.items.append(available_items[item_name])

        for room, saved_room in zip(rooms, saved["rooms"]):
            room.solved = saved_room["solved"]

            if not saved_room["has_item"]:
                room.item = None

        save_code = code

    menu = Menu(player, rooms, saves, save_code)
    menu.main_menu()


if __name__ == "__main__":
    main()
