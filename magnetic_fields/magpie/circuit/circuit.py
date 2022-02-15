from xml.dom import minidom

from circuit.wires import decodeWire

class Circuit:
    def __init__(self, wires):
        self.wires = wires

    def MagneticField(x, y):
        pass


def decodeCircuit(circuitNode: minidom.Element):
    
    wireNodes = circuitNode.getElementsByTagName('wire')
    wires = [ decodeWire(wire) for wire in wireNodes ]

    return Circuit(wires)