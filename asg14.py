class Employee:
    def __init__(self, name):
        self.name = name

class Department:
    def __init__(self, name, employee):
        self.name = name
        self.employee = employee

# Test
emp = Employee("John")
dept = Department("HR", emp)
print(dept.employee.name)  # Output: John