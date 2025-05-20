class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn         # Private

# Test
emp = Employee("Bob", 50000, "123-45-6789")
print(emp.name)        # Output: Bob
print(emp._salary)     # Output: 50000 (accessible, but convention discourages)
try:
    print(emp.__ssn)   # Raises AttributeError
except AttributeError:
    print("Cannot access private variable __ssn")
# Note: Can still access __ssn using _Employee__ssn, but this is discouraged
print(emp._Employee__ssn)  # Output: 123-45-6789