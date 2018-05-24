#!/usr/bin/env python

def func1():
    print("Hello World")

class Bogus:

    my_var1 = ""
    my_var2 = ""
    my_var3 = ""

    def hello(self):
        print("Hello " + self.my_var1 + ", " + self.my_var2 + " and " + self.my_var3)

    def not_hello(self):
        print("Bye " + self.my_var1 + ", " + self.my_var2 + " and " + self.my_var3)

    def __init__(self, var1, var2, var3):
        self.my_var1 = var1
        self.my_var2 = var2
        self.my_var3 = var3

class BogusNew(Bogus):

    def hello(self):
        print("Welcome " + self.my_var1 + ", " + self.my_var2 + " and " + self.my_var3)

    def __init__(self, var1, var2, var3):
        print("Doing something more here...")
        Bogus.__init__(self, var1, var2, var3)
        

if __name__ == "__main__":
    print("I'm the module 'world'")
