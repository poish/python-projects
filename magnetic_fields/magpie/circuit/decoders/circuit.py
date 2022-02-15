from magpie.circuit.types.circuit import Circuit
from magpie.circuit.decoders.wire import decodeWire

from magpie.circuit.decoders import circuitXML
from magpie.circuit.decoders import circuitJSON

decoderMap = {

    "json": circuitJSON.decodeJSON,
    "xml": circuitXML.decodeXML
}

def getDecoder(type):

    return decoderMap[type]