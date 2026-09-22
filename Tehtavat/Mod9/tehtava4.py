"""

Now we will program a car race. The travelled distance of a new car is initialized as zero.
At the beginning of the main program, create a list that consists of 10 car objects created using a loop.
The maximum speed of each new car is a random value between 100 km/h and 200 km/h.
The registration numbers are created as follows: “ABC-1”, “ABC-2” and so on.
Now the race begins. One per every hour of the race, the following operations are performed:

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h.
This is done using the accelerate method.
Each car is made to drive for one hour. This is done with the drive method.
The race continues until one of the cars has advanced at least 10,000 kilometers.
Finally, the properties of each car are printed out formatted into a clear table.

"""

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


def main():
    car = Car("ABC-123", 142)

    print(f"Registration number: {car.registration_number}")
    print(f"Maximum speed: {car.maximum_speed} km/h")
    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance} km")
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)

    print(f"Current speed: {car.current_speed}")

    car.accelerate(-200)
    print(f"Current speed: {car.current_speed}")

    car2 = Car("2", 142, 60, 2000)
    car2.drive(1.5)
    print(car2.travelled_distance)

    cars = []
    for i in range(1, 11):
        car_i = Car(f"ABC-{i}", random.randint(100, 200))
        cars.append(car_i)

    while True:
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

        if any(car.travelled_distance >= 10_000 for car in cars):
            break

    for car in cars:
        print(
            f"{car.registration_number} "
            f"{car.maximum_speed} km/h "
            f"{car.current_speed} km/h "
            f"{car.travelled_distance} km "
        )


if __name__ == "__main__":
    main()
