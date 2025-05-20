class Logger:
    def __init__(self):
        print("Object created!")
    
    def __del__(self):
        print("Object destroyed!")

# Test
log = Logger()  # Output: Object created!
del log        # Output: Object destroyed!
