#!/usr/bin/env python

import os
import re
import shutil
import textwrap
import xml.etree.ElementTree as ET

def slugify(txt):
  output = txt.lower()
  output = output.replace('+', 'p')
  output = re.sub(r'[\(\):]', '', output)
  output = re.sub(r'\W+', '-', output)
  return output.strip(' ').strip('-')

def getTitle(el):
  titleNodes = el.findall('title')
  if len(titleNodes) <= 0:
      raise Exception('Cannot find title')
  return titleNodes[0].text

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
    outFile.write('\n```')
    lang = root.attrib.get('lang')
    if lang is not None:
        if 'c' in lang:
            outFile.write(' c')
        elif 'C' in lang:
            outFile.write(' c++')
        elif 'J' in lang:
            outFile.write(' java')
        elif 'P' in lang:
            outFile.write(' python')
        elif 'M' in lang:
            outFile.write(' matlab')
    outFile.write('\n')
    outFile.write(parseText(root.text) + '\n')
    outFile.write('```\n\n')

def parseFigure(root, outFile):
    title = ''
    fileref = ''
    for child in root.getchildren():
        if child.tag == 'title':
            title = child.text
        elif child.tag  == 'graphic':
            fileref = child.attrib.get('fileref')
    if title is not None and len(title) > 0 and fileref is not None and len(fileref) > 0:
        outFile.write('![%s](%s)\n**%s**\n\n' % (title, fileref, title))

def parseChapter(root, outFile, outputDirectoryPath):
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
        elif child.tag == 'sect1':
            fileName = outputDirectoryPath + slugify(getTitle(child)) + ".md"
            print 'Generating ' + fileName
            if os.path.exists(fileName):
                raise Exception('sec1: "' + fileName + '" is existing')
            outFile = open(fileName, 'w')
            parseChapter(child, outFile, outputDirectoryPath)
            outFile.close()
        elif child.tag == 'sect2' or child.tag == 'sect3':
            parseChapter(child, outFile, outputDirectoryPath)
        elif child.tag == 'para':
            parsePara(child, outFile)
        elif child.tag == 'programlisting':
            parseProgramListing(child, outFile)
        elif child.tag == 'figure':
            parseFigure(child, outFile)

def parseBook(root, outFile, outputDirectoryPath):
    for child in root.getchildren():
        if child.tag == 'bookinfo':
            for subchild in child.getchildren():
                if subchild.tag == 'title':
                    outFile.write('# ' + subchild.attrib.get('name', subchild.text) + '\n\n')
        elif child.tag == 'preface':
            fileName = outputDirectoryPath + slugify(getTitle(child)) + ".md"
            print 'Generating ' + fileName
            if os.path.exists(fileName):
                raise Exception('preface: "' + fileName + '" is existing')
            outFile = open(fileName, 'w')
            parseChapter(child, outFile, outputDirectoryPath)
            outFile.close()
        elif child.tag == 'chapter':
            fileName = outputDirectoryPath + slugify(getTitle(child)) + ".md"
            print 'Generating ' + fileName
            if os.path.exists(fileName):
                raise Exception('chapter: "' + fileName + '" is existing')
            outFile = open(fileName, 'w')
            parseChapter(child, outFile, outputDirectoryPath)
            outFile.close()

def parseXMLFile(filePath):
    print 'Parse XML file: "' + filePath + '"'
    baseName = os.path.basename(filePath)
    inputDirectoryPath = os.path.dirname(filePath)
    outputDirectoryPath = os.path.basename(inputDirectoryPath) + '/'
    outputFilePath = outputDirectoryPath + baseName.replace('.xml', '.md')
    print 'Output file: ' + outputFilePath

    with open(filePath, 'r') as file:
      content = file.read()

    # deal with preprocessor instructions
    while True:
        mo = re.search(r'(&\w*;)', content)
        if not mo:
            break
        tag = mo.group(0)[1:-1] # remove the first and last characters
        output = ''
        if tag.endswith('_chapter'):
            with open(inputDirectoryPath + "/" + tag + '.xml', 'r') as includeFile:
                output = includeFile.read()
        else:
            # TODO: improve this
            output = tag
        content = content[:mo.start()] + output + content[mo.end():]

    root = ET.fromstring(content)

    outFile = open(outputFilePath, 'w')
    parseBook(root, outFile, outputDirectoryPath)
    outFile.close()


if __name__ == "__main__":
    webotsDirectory = '../webots/'
    documentationInputDirectories = [webotsDirectory + 'src/doc/guide/', webotsDirectory + 'src/doc/reference/']

    for inputDirectory in documentationInputDirectories:
        directoryName = os.path.basename(os.path.dirname(inputDirectory)) # guide or reference
        print 'Directory name: ' + directoryName

        intputFilePath = inputDirectory + directoryName + '.xml'
        print 'Input file name: ' + intputFilePath

        # recreate the target directory if any
        if os.path.exists(directoryName):
            shutil.rmtree(directoryName)
        os.makedirs(directoryName)
        # copy the png images
        shutil.copytree(webotsDirectory + 'doc/' + directoryName + '/png', directoryName + '/png')

        parseXMLFile(intputFilePath)
