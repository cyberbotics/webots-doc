#!/usr/bin/env python

import os
import re
import textwrap
import xml.etree.ElementTree as ET

def parsePara(root, outFile):
    if root.text:
        text = root.text.encode('utf-8')
        content = text.split('\n')
        text = ' '.join(map(lambda x: x.strip(), content)).strip()
        content = textwrap.wrap(text, width=80)
        for line in content:
            outFile.write(line.strip() + '\n')
        outFile.write('\n')

def parseChapter(root, outFile):
    for child in root.getchildren():
        if child.tag == 'title' and child.attrib.get('name', child.text):
            indent = 1
            if root.tag == 'chapter':
                indent = 2
            elif root.tag == 'sect1':
                indent = 3
            elif root.tag == 'sect2':
                indent = 4
            elif root.tag == 'sect3':
                indent = 5
            outFile.write('#' * indent + ' ' + child.attrib.get('name', child.text) + '\n\n')
        elif child.tag == 'sect1' or child.tag == 'sect2' or child.tag == 'sect3':
            parseChapter(child, outFile);
        elif child.tag == 'para':
            parsePara(child, outFile);

def parseBook(root, outFile):
    for child in root.getchildren():
        if child.tag == 'bookinfo':
            for subchild in child.getchildren():
                if subchild.tag == 'title':
                    outFile.write('# ' + subchild.attrib.get('name', subchild.text) + '\n\n')
        elif child.tag == 'preface':
            parseChapter(child, outFile)
        elif child.tag == 'require':
            print 'require' + child.attrib.get('tag')
            parseXMLFile(child.attrib.get('tag'))

def parseTopXmlElement(root, outFile):
    #outFile.write((u' '*indent + u'%s: %s' % (root.tag.title(), root.attrib.get('name', root.text))).encode('utf-8'))
    if root.tag == 'book':
        parseBook(root, outFile)
    elif root.tag == 'chapter':
        parseChapter(root, outFile)


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
    content = re.sub(r'&(.*)_chapter;', r'<require tag="' + inputDirectory + r'\1_chapter.xml" />', content)
    content = re.sub(r'&(\w*);', r'\1', content) # TODO: improve this

    root = ET.fromstring(content)

    outFile = open(outputFilePath, 'w')
    parseTopXmlElement(root, outFile)
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
