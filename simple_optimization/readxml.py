from xml.dom import minidom

# parse an xml file by name
mydoc = minidom.parse('circuit.xml')

wires = mydoc.getElementsByTagName('wire')

print(type(wires[0]))
controlPoints = wires[0].getElementsByTagName('cp')

def decodeCurve(controlPoints):
    x = []
    y = []
    for pt in controlPoints:
        x.append(pt.attributes['x'].value)
        y.append(pt.attributes['y'].value)

decodeCurve(controlPoints)