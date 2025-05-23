# Static Variables and Static Methods
# Assignment: Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.


class MathUtils:
    @staticmethod #allow to use it directly without instantiating and object with the class. Also we will not use self in here
    def add(a, b):
        return a + b

result = MathUtils.add(5,10)
print(result)

