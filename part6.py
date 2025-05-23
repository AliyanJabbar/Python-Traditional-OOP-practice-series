# Constructors and Destructors
# Assignment: Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).


class Logger: 
    def __init__(self): #run when we create an instance from this class 
        print("instance is created")
        
    def __del__(self): #runs when the instance is no longer refrence(used) somewhere.
        print("obj is destroyed")
        

obj = Logger()