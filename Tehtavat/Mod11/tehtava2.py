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


class ElectricCar(Car):
    def __init__(self, reg_number, max_speed, kilowatt_hours_capacity):
        self.kilowatt_hours_capacity = kilowatt_hours_capacity

        Car.__init__(self, reg_number, max_speed)


class GasolineCar(Car):
    def __init__(self, reg_number, max_speed, volume_liters):
        self.volume_litres = volume_liters
        Car.__init__(self, reg_number, max_speed)


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

    el_car = ElectricCar("ABC-15", 180, 52.5)
    gas_car = GasolineCar("ACD-123", 165, 33.2)
    el_car.accelerate(10)
    gas_car.accelerate(15)

    el_car.drive(3)
    gas_car.drive(3)

    print(
        f"{el_car.registration_number} "
        f"{el_car.maximum_speed} km/h "
        f"{el_car.current_speed} km/h "
        f"{el_car.travelled_distance} km "
    )
    print(
        f"{gas_car.registration_number} "
        f"{gas_car.maximum_speed} km/h "
        f"{gas_car.current_speed} km/h "
        f"{gas_car.travelled_distance} km "
    )


if __name__ == "__main__":
    main()
