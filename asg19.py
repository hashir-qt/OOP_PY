class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, x):
        return x * self.factor

# Test
m = Multiplier(5)
print(callable(m))  # Output: True
print(m(3))         # Output: 15