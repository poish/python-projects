from xml.dom import minidom

from magpie.curve.bezier import bezierDecoder
from magpie.curve.line import lineDecoder

def decodeCurve(curveNode: minidom.Element):

    curveType = getCurveType(curveNode) 
    decoder = getCurveDecoder(curveType)

    return decoder(curveNode)


def getCurveType(curveNode: minidom.Element):

    return curveNode.attributes['type'].value 


def getCurveDecoder(curveType: minidom.Element):

    decoders = {
        "line": lineDecoder,
        "bezier": bezierDecoder
    }

    return decoders[curveType]

