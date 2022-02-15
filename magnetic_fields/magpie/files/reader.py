from xml.dom import minidom


def read(path: str):

    document = minidom.parse(path)
    return document.getElementsByTagName('circuit')[0]

