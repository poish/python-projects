from xml.dom import minidom

from magpie.circuit.types.circuit import Circuit
from magpie.circuit.decoders.wire import decodeWire

def decodeXML(circuitNode: minidom.Element):
    
    wireNodes = circuitNode.getElementsByTagName('wire')
    wires = [ decodeWire(wire) for wire in wireNodes ]

    return Circuit(wires)
