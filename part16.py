#  Function Decorators
# Assignment: Write a decorator function log_function_call that prints "Function is being called" before a function executes. Apply it to a function say_hello().



def log_function_call(func):
    print("Function is being called")
    func()

@log_function_call
def say_hello():
    print("Function is saying hello...")
