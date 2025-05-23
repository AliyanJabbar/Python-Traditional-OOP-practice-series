# Make a Custom Class Iterable
# Assignment: Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown: 
    def __init__(self,starter):
        self.current = starter
        
    def __iter__(self): # This method is called when the object is iterated over
        self.current -= 1
        return self
    
    def __next__(self): # This method is called to get the next value in the iteration
        if self.current < 0: 
            raise StopIteration
        else : 
            current = self.current
            self.current -= 1
            return current


# Example usage
countdown = Countdown(100)
for number in countdown: 
    print(number)
    
print("End of countdown")