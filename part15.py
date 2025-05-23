# Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.


class A: 
    def show(self):
        print("A class is showing")

class B(A):
    def show(self):
        print("B class is showing")

class C(A):
    def show(self):
        print("C class is showing")

class D(B,C):
    pass

d = D()
d.show()  # Output: B class is showing because of mro -> method resolution order. 
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
# means D class will first look for the method in B class, if not found then it will look in C class and so on.