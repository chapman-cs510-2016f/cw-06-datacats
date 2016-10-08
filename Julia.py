#!/usr/bin/env python3

def julia(c, max=100):
    def f(z):
        if abs(z) > 2:
            return 1
        n = 0
        test = True
        while test:
            z = z**2 + c
            n += 1
            if n == max:
                test = False
                n = 0
            elif abs(z) > 2:
                test = False
        print(n)
        return n
    return f