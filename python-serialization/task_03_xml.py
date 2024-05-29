#!/usr/bin/python3
"""
Serialization and deserialization using XML as an alternative format to JSON.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
        Take a Python dictionary and a filename as parameters.
        It should serialize the dictionary into XML
        and save it to the given filename.
    """

    root = ET.Element('data')
    for key, value in dictionary.items():
        tree = ET.SubElement(root, key)
        tree.text = value
    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8')


def deserialize_from_xml(filename):
    """
        Take a filename as its parameter,
        read the XML data from that file,
        and return a deserialized Python dictionary.
    """

    dictionary = {}
    tree = ET.parse(filename)
    root = tree.getroot()
    for child in root:
        dictionary[child.tag] = child.text
    return (dictionary)
