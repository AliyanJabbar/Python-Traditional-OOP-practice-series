# Static Methods
# Assignment: Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.


class TemperatureConverter:
    @staticmethod #Static Method -> does not take the class(cls) or instanse(self) as the first argument just directly use it by using className.method
    def celsius_to_fahrenheit(c):
        return (c * 9 / 5) + 32
    
print(TemperatureConverter.celsius_to_fahrenheit(0))  # Output: 32.0
print(TemperatureConverter.celsius_to_fahrenheit(36.7))  # Output: 98.06
