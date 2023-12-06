# Simple Class and Object

# Define a simple class for a Car
class Car:
    # Constructor method to initialize the car's attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    # Method to get a formatted description of the car
    def get_description(self):
        return f"{self.year} {self.make} {self.model}"

    # Method to read the odometer
    def read_odometer(self):
        return f"Odometer Reading: {self.odometer_reading} miles"

    # Method to update the odometer reading
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
            print("Odometer updated successfully.")
        else:
            print("You cannot roll back the odometer!")

# Create an instance of the Car class
my_car = Car(make="Toyota", model="Camry", year=2022)

# Display the car's description
print(f"Car Description: {my_car.get_description()}")

# Read the initial odometer reading
print(my_car.read_odometer())

# Update the odometer reading
my_car.update_odometer(1000)

# Attempt to roll back the odometer (this should fail)
my_car.update_odometer(500)
