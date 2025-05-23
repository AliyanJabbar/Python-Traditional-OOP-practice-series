# Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.



class Employee: 
    def __init__(self,name,salary,ssn):
        self.name = name #public
        self._salary = salary #protected
        self.__ssn = ssn #private
        
        
employee = Employee("Ali", 700000, "123-45-6789")
print(employee.name) # accessible
print(employee._salary) # accessible
# print(employee.__ssn) # not accessible, will raise an AttributeError -> AttributeError: 'Employee' object has no attribute '__ssn'
# print(employee._Employee__ssn) #printing the private variable using name mangling
