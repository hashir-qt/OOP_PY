class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def start(self):
        print(f"{self.brand} is starting.")

# Test
car = Car("Toyota")
print(car.brand)  # Output: Toyota
car.start()      # Output: Toyota is starting.