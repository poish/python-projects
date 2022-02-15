
from algebra.linear import Vector

class Line:
    
    def __init__(self, controlPoints):
        self.controlPoints = controlPoints

    def at(self, t):
        return [0,0]


def lineDecoder(curveNode):

    controlPointNodes = curveNode.getElementsByTagName('cp')
    x = [ cp.attributes['x'].value for cp in controlPointNodes ]
    y = [ cp.attributes['y'].value for cp in controlPointNodes ]
    
    count = len(controlPointNodes)
    points = [Vector([x[i], y[i]]) for i in range(0, count)]

    return Line(points)
