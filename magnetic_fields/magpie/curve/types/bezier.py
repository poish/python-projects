import math
from xml.dom import minidom
from algebra.linear import Vector

class Bezier:

    def __init__(self, controlPoints):
        self.A = controlPoints[0]
        self.B = controlPoints[1]
        self.C = controlPoints[2]
        self.C = controlPoints[3]
        
    def at(self, t):
        ct = 1 - t
        x = pow(ct, 3)*self.A[0] + 3*t*pow(ct,2)*self.B[0] + 3*pow(t,2)*ct*self.C[0] + pow(t,3)*self.D[0]
        y = pow(ct, 3)*self.A[1] + 3*t*pow(ct,2)*self.B[1] + 3*pow(t,2)*ct*self.C[1] + pow(t,3)*self.D[1]

        return [x,y]
    
    def tangent(self, t):

        return [0,0]

    def dicretizeCurve(self, step):

        L = self.length(0,1)
        intervals = [[0,1, L]] # A list with single interval

        while True:
            updatedIntervals = []
            for s in intervals:

                if s[2] > step: # if the length of the interval is larger than the step, split the interval into two

                    midpoint = 0.5*(s[0] + s[1])

                    A  = self.length(s[0],midpoint)
                    updatedIntervals.append([s[0], midpoint, A])

                    B = self.length(midpoint,s[1])
                    updatedIntervals.append([midpoint, s[1], B])
            
                else:
                    updatedIntervals.append(s)

            if len(updatedIntervals) == 0:
                break

            intervals = updatedIntervals
            


    def length(self, limits):
        pass

    def __repr__(self):
        pass

def bezierDecoder(curveNode):

    controlPointNodes = curveNode.getElementsByTagName('cp')
    x = [ cp.attributes['x'].value for cp in controlPointNodes ]
    y = [ cp.attributes['y'].value for cp in controlPointNodes ]
    
    count = len(controlPointNodes)
    points = [Vector(x[i], y[i]) for i in range(0, count)]

    return Bezier(points)
