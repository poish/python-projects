import numpy as np
import matplotlib.pyplot as plt

from xml.dom import minidom

# parse an xml file by name
from magpie.files.reader import read
from magpie.circuit.wire import decodeWire

circ = read('circuit.xml')

wireNodes = circ.getElementsByTagName('wire')
 
wires = [ decodeWire(wire) for wire in wireNodes ]

for w in wires:
    print(w)