class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        print(f"{self.name} says Woof!")

# Test
dog = Dog("Buddy", "Golden Retriever")
dog.bark()  # Output: Buddy says Woof!