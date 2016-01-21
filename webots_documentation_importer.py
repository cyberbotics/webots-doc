#!/usr/bin/env python

import os
import re
import textwrap
import xml.etree.ElementTree as ET

def parseText(txt):
    if txt is None:
        return ''
    return txt.encode('utf-8')

def parsePara(root, outFile):
    # para included tags:
    #     bold, command, computeroutput, email, emphasis, filename, function,
    #     guibutton, guilabel, guimenu, guimenuitem, guisubmenu, hlink,
    #     inlinegraphic, keycap, math, parameter, programlisting, trademark
    #     ulink, xref
    text = ''
    if root.text:
        text += parseText(root.text)
    for child in root.getchildren():
        if child.tag == 'bold' and child.text:
            text += '**' + parseText(child.text) + '**'
        elif child.tag == 'emphasis' and child.text:
            text += '*' + parseText(child.text) + '*'
        elif child.tag == 'filename' and child.text:
            text += '"' + parseText(child.text) + '"'
        elif child.text:
            text += '`' + parseText(child.text) + '`'
        text += parseText(child.tail)
    text += parseText(root.tail)

    content = text.split('\n')
    text = ' '.join(map(lambda x: x.strip(), content)).strip()
    content = textwrap.wrap(text, width=80)
    for line in content:
        outFile.write(line.strip() + '\n')
    outFile.write('\n')

def parseProgramListing(root, outFile):
    outFile.write('\n```\n')
    outFile.write(parseText(root.text) + '\n')
    outFile.write('```\n\n')

def parseChapter(root, outFile):
    for child in root.getchildren():
        if child.tag == 'title' and child.attrib.get('name', child.text):
            indent = 0
            if root.tag == 'chapter':
                indent = 1
            elif root.tag == 'sect1' or root.tag == 'preface':
                indent = 2
            elif root.tag == 'sect2':
                indent = 3
            elif root.tag == 'sect3':
                indent = 4
            else:
                raise Exception('Unsupported type: ' + root.tag)
            outFile.write('#' * indent + ' ' + child.attrib.get('name', child.text) + '\n\n')
        elif child.tag == 'sect1' or child.tag == 'sect2' or child.tag == 'sect3':
            parseChapter(child, outFile)
        elif child.tag == 'para':
            parsePara(child, outFile)
        elif child.tag == 'programlisting':
            parseProgramListing(child, outFile)

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
