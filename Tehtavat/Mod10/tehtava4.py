import random


class Car:
    def __init__(
        self,
        registration_number=0,
        maximum_speed=0,
        current_speed=0,
        travelled_distance=0,
    ):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = current_speed
        self.travelled_distance = travelled_distance

    def accelerate(self, change):
        if self.current_speed + change > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed + change < 0:
            self.current_speed = 0
        else:
            self.current_speed += change

    def drive(self, hours):
        self.travelled_distance += hours * self.current_speed


class Race:
    def __init__(self, name, dist_km, cars):
        self.name = name
        self.dist_km = dist_km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        for car in self.cars:
            print(
                f"{car.registration_number} "
                f"{car.maximum_speed} km/h "
                f"{car.current_speed} km/h "
                f"{car.travelled_distance} km "
            )

    def race_finished(self):
        if any(car.travelled_distance >= self.dist_km for car in self.cars):
            return True
        else:
            return False


def main():

    cars = []
    for i in range(1, 11):
        car_i = Car(f"ABC-{i}", random.randint(100, 200))
        cars.append(car_i)

    race = Race("Grand Demolition Derby", 8000, cars)

    i = 0
    while race.race_finished() == False:
        race.hour_passes()
        i += 1
        if i % 10 == 0:
            race.print_status()
    race.print_status()


if __name__ == "__main__":
    main()
