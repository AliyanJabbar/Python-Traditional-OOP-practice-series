# Aggregation
# Assignment: Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.



class Employee:
    def __init__(self,name):
        self.name = name 

class Department:
    def __init__(self,employee: Employee):
        self.employee = employee
        print(f"{self.employee.name} works here in this department.")
employee1 = Employee("Aliyan")
department_store = Department(employee1)