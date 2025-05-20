class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        print(f"Engine with {self.horsepower} HP started.")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine
    
    def start(self):
        self.engine.start()

# Test
engine = Engine(200)
car = Car("Honda", engine)
car.start()  # Output: Engine with 200 HP started.