#!/usr/bin/env python

import os
import re
import xml.etree.ElementTree as ET


webotsDirectory = '../webots/'
documentationInputDirectories = [webotsDirectory + 'src/doc/guide/', webotsDirectory + 'src/doc/reference/']

indent = 0

def printRecur(root, outFile):
    outFile.write((u' '*indent + u'%s: %s' % (root.tag.title(), root.attrib.get('name', root.text))).encode('utf-8'))
    global indent
    indent += 4
    for elem in root.getchildren():
        printRecur(elem, outFile)
    indent -= 4


def parseXMLFile(filePath):
    print 'Parse XML file: "' + filePath + '"'
    baseName = os.path.basename(filePath)
    directoryName = os.path.basename(os.path.dirname(filePath))
    outputFilePath = directoryName + '/' + baseName.replace('.xml', '.md')
    print 'Output file: ' + outputFilePath

    if not os.path.exists(directoryName):
        os.makedirs(directoryName)

    with open(filePath, 'r') as file:
      content = file.read()
    # xml.etree doesn't support the ENTITY - SYSTEM tags
    # => the following line are converting them to a custom <require> tag
    content = re.sub(r'&(.*)_chapter;', r'<require tag="' + inputDirectory + r'\1.xml" />', content)

    root = ET.fromstring(content)

    outFile = open(outputFilePath, 'w')
    printRecur(root, outFile)
    outFile.close()


for inputDirectory in documentationInputDirectories:
    directoryName = os.path.basename(os.path.dirname(inputDirectory)) # guide or reference
    print 'Directory name: ' + directoryName

    intputFilePath = inputDirectory + directoryName + '.xml'
    print 'Input file name: ' + intputFilePath

    parseXMLFile(intputFilePath)
