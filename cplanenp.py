#!/usr/bin/env python3

import abscplane as ab
import numpy as np
import pandas as pd

class ComplexPlaneNP(ab.AbsComplexPlane):

    def __init__(self, xmin=-5.0, xmax=5.0, xlen=10, ymin=-5.0, ymax=5.0, ylen=10, plane= [], f=lambda x:x):
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
        y, x = np.meshgrid(b,a)
        z = x + y*1j

        # Creating a list of each x and y value to be used in our pandas implementation for column and row names.
        x_val = []
        y_val = []
        inc_x = (self.xmax - self.xmin) / (self.xlen)
        inc_y = (self.ymax - self.ymin) / (self.ylen)
        for i in range(self.xlen + 1):
            x_val.append(self.xmin + (i * inc_x) )
        for j in range(self.ylen + 1):
            y_val.append(str(self.ymin + (j * inc_y)) + "*j")

        f = pd.DataFrame(z, x_val, y_val)
        self.plane = f.T

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
