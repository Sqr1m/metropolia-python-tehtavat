"""
Write a Car class that has the following properties: registration number, maximum speed,
current speed and travelled distance.
Add a class initializer that sets the first two of the properties based on parameter values.
The current speed and travelled distance of a new car must be automatically set to zero.
Write a main program where you create a new car (registration number ABC-123,
maximum speed 142 km/h). Finally, print out all the properties of the new car.
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


def main():
    car = Car("ABC-123", 142)
    print(f"Registration number: {car.registration_number}")
    print(f"Maximum speed: {car.maximum_speed} km/h")
    print(f"Current speed: {car.current_speed} km/h")
    print(f"Travelled distance: {car.travelled_distance} km")


if __name__ == "__main__":
    main()
