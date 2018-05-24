#!/usr/bin/env python

from mytest import *

def main():
    func1()
    func2()
    func3()

    my_bogus = Bogus("Luise", "Olivia", "Minna")
    my_bogus.hello()

if __name__ == "__main__":
    main()
