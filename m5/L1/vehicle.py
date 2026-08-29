class Vehicle:
    fuel = "petrol"
    def __init__(self, speed, milage):
        self.speed = speed
        self.milage = milage

car = Vehicle(100, 3)
bike = Vehicle(80, 5)

print(car.speed)
print()
print(bike.milage)