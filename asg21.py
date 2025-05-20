class Countdown:
    def __init__(self, start):
        self.start = start
        self.current = start + 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.current -= 1
        if self.current < 0:
            raise StopIteration
        return self.current

# Test
for num in Countdown(3):
    print(num)  # Output: 3, 2, 1, 0