#!/usr/bin/env python

import os
import re
import xml.etree.ElementTree as ET


def parsePara(root, outFile):
    outFile.write(((root.attrib.get('name', root.text)) + '\n').encode('utf-8'))

def parseSection(root, outFile):
    for child in root.getchildren():
        if child.tag == 'title':
            outFile.write('## ' + child.attrib.get('name', child.text) + '\n\n')
        elif child.tag == 'para':
            parsePara(child, outFile);

def parseBook(root, outFile):
    for child in root.getchildren():
        if child.tag == 'bookinfo':
            for subchild in child.getchildren():
                if subchild.tag == 'title':
                    outFile.write('# ' + subchild.attrib.get('name', subchild.text) + '\n\n')
        elif child.tag == 'preface':
            parseSection(child, outFile)

def parseChapter(root, outFile):
    pass

def parseXmlElement(root, outFile):
    #outFile.write((u' '*indent + u'%s: %s' % (root.tag.title(), root.attrib.get('name', root.text))).encode('utf-8'))
    if root.tag == 'book':
        parseBook(root, outFile)
    elif root.tag == 'chapter':
        parseChapter(root, outFile)
    else:
        for child in root.getchildren():
            parseXmlElement(child, outFile)


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
    parseXmlElement(root, outFile)
    outFile.close()


if __name__ == "__main__":
    webotsDirectory = '../webots/'
    documentationInputDirectories = [webotsDirectory + 'src/doc/guide/', webotsDirectory + 'src/doc/reference/']

    for inputDirectory in documentationInputDirectories:
        directoryName = os.path.basename(os.path.dirname(inputDirectory)) # guide or reference
        print 'Directory name: ' + directoryName

        intputFilePath = inputDirectory + directoryName + '.xml'
        print 'Input file name: ' + intputFilePath

        parseXMLFile(intputFilePath)
