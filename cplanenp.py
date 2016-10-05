#!/usr/bin/env python3

import abscplane as ab
import numpy as np
import pandas as pd

class ComplexPlaneNP(ab.AbsComplexPlane):

    def __init__(self, xmin=-5, xmax=5, xlen=10, ymin=-5, ymax=5, ylen=10, plane= [], f=lambda x:x):
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        self.plane = plane
        self.f = f

        self.refresh()
        
    def refresh(self):
        a= np.linspace(self.xmin, self.xmax, self.xlen+1) 
        b= np.linspace(self.ymin, self.ymax, self.ylen+1)
        x, y = np.meshgrid(a,b)
        z = x + y*1j
        self.plane = z[:]
        # For testing purposes, print out the plane to check values
        print(self.plane)
        
    def zoom(self, xmin, xmax, xlen, ymin, ymax, ylen):
        self.xmin = xmin
        self.xmax = xmax
        self.xlen = xlen
        self.ymin = ymin
        self.ymax = ymax
        self.ylen = ylen
        
        self.refresh()

    def set_f(self, f):
        self.f = f
        self.refresh()
        
       
    def julia(c, max=100):
        def f(z): 
            return z**2 + c
        return f 