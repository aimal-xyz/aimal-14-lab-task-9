class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start(self):
        print("The car is starting.")
car1 = Car("Honda", "White")

car1.start()