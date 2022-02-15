import magpie.curve.decoder as decoder
import values

from xml.dom import minidom

class Wire:
    def __init__(self, curve, current):
        self.curve = curve
        self.current = current

    def __repr__(self):
        return f"curve: {self.curve}, I: {self.current}"

def decodeWire(wireNode: minidom.Element):

    curveNode = wireNode.getElementsByTagName('curve')[0]   # There should be only one shape node
    scalarNode = wireNode.getElementsByTagName('scalar')[0]
    

    curve = decoder.decodeCurve(curveNode)
    current = values.decodeScalar(scalarNode)
    return Wire(curve, current)
