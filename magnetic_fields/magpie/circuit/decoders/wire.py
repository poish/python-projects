

def decodeWire(wireNode: minidom.Element):

    curveNode = wireNode.getElementsByTagName('curve')[0]   # There should be only one shape node
    scalarNode = wireNode.getElementsByTagName('scalar')[0]
    

    curve = decodeCurve(curveNode)
    current = values.decodeScalar(scalarNode)
    return Wire(curve, current)
