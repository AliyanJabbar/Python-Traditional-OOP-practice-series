# Class Decorators
# Assignment: Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.


class add_greeting:
    def __init__(self, cls):
        def greet(self):
            return "Hello from Decorator!"
        cls.greet = greet
        self.cls = cls

    def __call__(self,*arg):
        return self.cls(*arg)


@add_greeting
class Person:
    def __init__(self, name):
        self.name = name


p1 = Person("Aliyan")
print(p1.greet())  # Output: Hello from Decorator!
