#!/usr/bin/env python3
"""Julia
This module has a method called Julia, which takes in the following arguments:
    c           : a complex parameter
    max (int)   : an optional positive integer, defaulted at 100
and returns the function f.
The function f takes in the argument
    z           : a complex parameter
and returns an integer value, n.
Upon being called, the function f will do the following operation z = z**2 + c, and will keep track of how many
iterations of the operation will it take before the absolute value of z exceeds the value of 2, stores that value in the variable n
then returns n.
The method will return 0 if n exceeds the max value.
"""
def julia(c, max=100):
    # error message to check that max is a positive integer value
    if max < 1:
        print("Please input a positive integer value for max")
        return 0

    # function f
    def f(z):
        # checks to make sure that the value of z is already greater than 2
        if abs(z) > 2:
            return 1

        # setting our initial variables
        n = 0
        test = True

        # While loop that will iterate as many times as needed until the value of z exceeds 2, or if the value of n exceeds max
        while test:
            z = z**2 + c
            n += 1
            if n == max:
                test = False
                n = 0
            elif abs(z) > 2:
                test = False
        return n
    return f