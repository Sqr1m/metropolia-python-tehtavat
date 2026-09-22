class Elevator:
    def __init__(self, bottom_floor, top_floor):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.current_floor = bottom_floor

    def go_to_floor(self, floor):
        while floor != self.current_floor:
            if floor > self.current_floor:
                self.floor_up()
            else:
                self.floor_down()

    def floor_up(self):
        self.current_floor += 1
        print(self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print(self.current_floor)


class Building:
    def __init__(self, bottom_floor, top_floor, number_of_elevators):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.number_of_elevators = number_of_elevators

        self.l_n_f_e = []
        for i in range(self.number_of_elevators):
            self.l_n_f_e.append(Elevator(bottom_floor, top_floor))

    def run_elevator(self, number_of_elevator, destination_floor):
        self.l_n_f_e[number_of_elevator].go_to_floor(destination_floor)

    def fire_alarm(self):
        for i in range(self.number_of_elevators):
            self.run_elevator(i, self.bottom_floor)


def main():
    el = Elevator(1, 10)
    el.go_to_floor(6)
    el.go_to_floor(1)
    buil = Building(1, 10, 3)
    buil.run_elevator(0, 6)
    buil.run_elevator(1, 8)
    buil.fire_alarm()


if __name__ == "__main__":
    main()
