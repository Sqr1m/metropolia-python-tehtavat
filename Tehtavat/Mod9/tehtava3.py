"""
Again, extend the program by adding a new drive method that receives the number of hours as a parameter.
The method increases the travelled distance by how much the car has travelled in constant speed in the given time.
Example: The travelled distance of car object is 2000 km. The current speed is 60 km/h.
Method call car.drive(1.5) increases the travelled distance to 2090 km.

"""


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


if __name__ == "__main__":
    main()
