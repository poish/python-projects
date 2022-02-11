from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('circuit.xml')

wire = mydoc.getElementsByTagName('wire')[0]

def decodeWire(wireNode):
    
    shapeNode = wireNode.getElementsByTagName('shape')[0]
    valueNodes = wireNode.getElementsByTagName('value')
    