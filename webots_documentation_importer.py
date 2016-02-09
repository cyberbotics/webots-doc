#!/usr/bin/env python

import glob
import os
import re
import shutil
import textwrap
import xml.etree.ElementTree as ET
import pdb # break with pdb.set_trace()


def slugify(txt):
  output = txt.lower()
  output = output.replace('+', 'p')
  output = re.sub(r'[\(\):`]', '', output)
  output = re.sub(r'\^\(TM\)', '', output)
  output = re.sub(r'\W+', '-', output)
  return output.strip(' ').strip('-')

def simplifySpaces(filename):
    with open(filename, 'r') as file:
        content = file.read()

    content = re.sub(r'[ \t]*\n', '\n', content)
    content = re.sub(r'\n\n\n*', '\n\n', content)

    outFile = open(filename, 'w')
    outFile.write(content)
    outFile.close()

class BookParser:
    def __init__(self, webotsDirectoryPath, bookName):
        self.bookName = bookName
        self.root = None
        
        self.outputDirectoryPath = self.bookName + '/'

        # recreate the target directory if any
        if os.path.exists(bookName):
            shutil.rmtree(bookName)
        os.makedirs(bookName)
        # copy the png images
        shutil.copytree(webotsDirectoryPath + 'doc/' + bookName + '/png', bookName + '/png')
        shutil.copytree(webotsDirectoryPath + 'doc/' + bookName + '/pdf', bookName + '/pdf')
        for fl in glob.glob(bookName + '/pdf/*.pdf'):
            os.remove(fl)


    def parseXMLFile(self, filePath):
        print 'Parse XML file: "' + filePath + '"'
        baseName = os.path.basename(filePath)
        inputDirectoryPath = os.path.dirname(filePath)

        with open(filePath, 'r') as file:
            content = file.read()

        # deal with preprocessor instructions
        while True:
            mo = re.search(r'&(\w*_chapter);', content)
            if not mo:
                break
            tag = mo.group(1)
            output = ''
            with open(inputDirectoryPath + '/' + tag + '.xml', 'r') as includeFile:
                output = includeFile.read()
            content = content[:mo.start()] + output + content[mo.end():]

        # dealt with `procedure` and `step` nodes
        content = content.replace('<procedure>', '<orderedlist>') \
                         .replace('</procedure>', '</orderedlist>') \
                         .replace('<step>', '<listitem>') \
                         .replace('</step>', '</listitem>')

        self.root = ET.fromstring(content)

    def exportToc(self):
        if self.root is None:
            raise Exception('Cannot export toc')

        outputFilePath = self.outputDirectoryPath + 'toc.md'
        print 'Generating toc: ' + outputFilePath

        outFile = open(outputFilePath, 'w')

        outFile.write('# Table of contents\n\n')
        chapterCounter = 0
        for chapterNode in self.root.findall('.//chapter'):
            chapterCounter += 1
            title = self.getTitle(chapterNode)
            outFile.write('%d. [%s](%s)\n' % (chapterCounter, title, self.bookName + '/' + slugify(title) + '.md'))
            sectionCounter = 0
            for sectionNode in chapterNode.findall('.//sect1'):
                sectionCounter += 1
                title = self.getTitle(sectionNode)
                outFile.write('    %d. [%s](%s)\n' % (sectionCounter, title, self.bookName + '/' + slugify(title) + '.md'))
        outFile.close()
        simplifySpaces(outputFilePath)

    def export(self):
        if self.root is None:
            raise Exception('Cannot export book')

        outputFilePath = self.outputDirectoryPath + self.bookName + '.md'
        print 'Generating file: ' + outputFilePath
        outFile = open(outputFilePath, 'w')
        self.parseBook(self.root, outFile)
        outFile.close()
        simplifySpaces(outputFilePath)

    def getTitle(self, node):
        title = None
        if node.tag == 'title':
            title = node
        else:
            titleNodes = node.findall('title')
            if len(titleNodes) <= 0:
                return ''
            title = titleNodes[0]

        text = ''
        if title.text:
            text += title.text
        for child in title.getchildren():
            if child.text:
                if child.tag == 'trademark':
                    text += '*' + child.text + '*^(TM)'
                elif child.tag == 'function' or child.tag == 'math':
                    text += '`' + child.text + '`'
                else:
                    raise Exception('Unsupported type: ' + child.tag)
            if child.tail:
                text += child.tail
        text += title.tail
        text = text.strip()
        text = re.sub(r'\n', '', text)
        text = re.sub(r'  *', ' ', text)

        return text

    def parseText(self, txt, protect, removeTrailingSpaces):
        if txt is None:
            return ''
        output = txt.encode('utf-8')

        m = re.search(r'\&\w*;', output)
        if m:
          print m.group(0)

        if protect:
            output = output.replace('_', '\\_')
        if removeTrailingSpaces:
            output = re.sub(r'[ \t]*\n', '\n', output)
            output = re.sub(r'[ \t]*$', '', output)
            output = re.sub(r'\n*$', '', output)
        return output

    def formatText(self, text):
        text.strip()
        content = text.split('\n')
        text = ' '.join(map(lambda x: x.strip(), content)).strip()
        content = textwrap.wrap(text, width=80)
        output = ''
        for i in range(0, len(content)):
            line = content[i]
            output += line.strip()
            if i != len(content) - 1:
                output += '\n'
        return output

    def parsePara(self, node, outFile, indent=0, inList=False, mergeCarriageReturns=False):
        # para included tags:
        #     bold, command, computeroutput, email, emphasis, filename, function,
        #     guibutton, guilabel, guimenu, guimenuitem, guisubmenu, hlink,
        #     inlinegraphic, keycap, math, parameter, programlisting, trademark
        #     ulink, xref
        text = ''
        if node.text:
            text += self.parseText(node.text, True, False)
        for child in node.getchildren():
            if child.text:
                if child.tag == 'bold':
                    text += '**' + self.parseText(child.text, True, False) + '**'
                elif child.tag == 'email':
                    text += '[' + self.parseText(child.text, True, False) + '](mailto:' + self.parseText(child.text, True, False) + ')'
                elif child.tag == 'emphasis':
                    text += '*' + self.parseText(child.text, True, False) + '*'
                elif child.tag == 'filename':
                    text += '"' + self.parseText(child.text, True, False) + '"'
                elif child.tag == 'trademark':
                    text += '*' + self.parseText(child.text, True, False) + '*^(TM)'
                elif child.tag == 'ulink':
                    text += '[' + self.parseText(child.text, True, False) + '](' + child.attrib.get('url') + ')'
                elif child.tag == 'programlisting':
                    # flush text
                    text = self.formatText(text)
                    content = text.split('\n')
                    for i in range(0, len(content)):
                        line = content[i]
                        if len(line.strip()) > 0:
                            outFile.write(' ' * indent + line)
                        outFile.write('\n')
                    outFile.write('\n')
                    text = ''
                    if inList and indent == 0:
                        indent += 4
                    if indent > 0:
                        self.parseProgramListing(child, outFile, indent + 4)
                    else:
                        self.parseProgramListing(child, outFile)
                    outFile.write('\n\n')
                else:
                    text += '`' + self.parseText(child.text, False, False) + '`'
            else: # not a text tag
                if child.tag == 'space':
                    text += '&nbsp;'
            text += self.parseText(child.tail, True, False)
        text += self.parseText(node.tail, True, False)

        if mergeCarriageReturns:
            text = re.sub(r'\n', ' ', text)
            text = re.sub(r'[ \t]+', ' ', text)
            outFile.write(text)
        else:
            text = self.formatText(text)

            content = text.split('\n')
            for i in range(0, len(content)):
                line = content[i]
                if len(line.strip()) > 0:
                    outFile.write(' ' * indent + line)
                if i != len(content) - 1:
                    outFile.write('\n')


    def parseProgramListing(self, node, outFile, indent=0, prefix=''):
        output = '\n'
        if indent == 0:
            output += '```'
            lang = node.attrib.get('lang')
            if lang is not None:
                if 'c' in lang:
                    output += ' c'
                elif 'C' in lang:
                    output += ' c++'
                elif 'J' in lang:
                    output += ' java'
                elif 'P' in lang:
                    output += ' python'
                elif 'M' in lang:
                    output += ' matlab'
            output += '\n'

        text = self.parseText(node.text, False, True)
        content = text.split('\n')
        for i in range(0, len(content)):
            line = content[i]
            output += prefix + ' ' * indent + line
            if i != len(content) - 1:
                output += '\n'

        if indent == 0:
            output += '\n```\n\n'

        outFile.write(output)

    def parseFigure(self, node, outFile):
        title = self.getTitle(node)
        if len(title) == 0:
            raise Exception('figure title not found')
        fileref = ''
        for child in node.getchildren():
            if child.tag == 'title':
                pass
            elif child.tag  == 'graphic':
                fileref = child.attrib.get('fileref')
            else:
                raise Exception('Unsupported type: ' + child.tag)
        if fileref is not None and len(fileref) > 0:
            if fileref.endswith('.pdf'):
                fileref += '.png'
            outFile.write('\n%%figure "%s"\n![%s](%s)\n%%end\n\n' % (title, title, fileref))

    def parseList(self, node, outFile, ordered):
        items = node.findall('./listitem')
        supplementaryCarriageReturnBetweenItems = len(node.findall('./listitem')) != len(node.findall('./listitem/')) 
        counter = 0
        for item in items:
            counter = counter + 1
            if ordered:
                outFile.write('%d. ' % (counter,))
            else:
                outFile.write('- ')

            firstParaChild = True
            for child in item.getchildren():
                if child.tag == 'para':
                    if firstParaChild:
                        self.parsePara(child, outFile, 0, True)
                        firstParaChild = False
                    else:
                        self.parsePara(child, outFile, 4, True)
                elif child.tag == 'figure':
                    self.parseFigure(child, outFile)
                elif child.tag == 'programlisting':
                    self.parseProgramListing(child, outFile, 8)
                elif child.tag == 'note':
                    self.parseIconPara(child, outFile, 4)
                else:
                    raise Exception('Unsupported type: ' + child.tag)
                outFile.write('\n')
                if supplementaryCarriageReturnBetweenItems:
                    outFile.write('\n')
        outFile.write('\n')

    def parseTable(self, node, outFile):
        title = self.getTitle(node)
        header = len(node.findall('.//thead')) == 1
        nCols = int(node.findall('tgroup')[0].attrib.get('cols'))

        if len(title) > 0:
            outFile.write('%%figure "%s"\n' % (title))

        if not header:
            outFile.write('| ' * (1 + nCols) + '\n')
            firstEntry = True
            for i in range(0, nCols):
                if firstEntry:
                    outFile.write('| ')
                    firstEntry = False
                else:
                    outFile.write(' | ')
                outFile.write('---')
            outFile.write(' |\n')

        line = 0
        for rowNode in node.findall('.//row'):
            line += 1
            firstEntry = True
            for entryNode in rowNode.findall('entry'):
                if firstEntry:
                    outFile.write('| ')
                    firstEntry = False
                else:
                    outFile.write(' | ')
                self.parsePara(entryNode, outFile, mergeCarriageReturns=(not header))
            outFile.write(' |\n')
            if line == 1 and header:
                firstEntry = True
                for i in range(0, nCols):
                    if firstEntry:
                        outFile.write('| ')
                        firstEntry = False
                    else:
                        outFile.write(' | ')
                    outFile.write('---')
                outFile.write(' |\n')

        if len(title) > 0:
            outFile.write('%%end\n')

        outFile.write('\n')

    def parseIconPara(self, node, outFile, indent=0):
        outFile.write(' ' * indent + '> **' + node.tag + '**: ')

        firstItem = True
        for child in node.getchildren():
            if child.tag == 'para':
                if firstItem:
                    firstItem = False
                else:
                    outFile.write(' ' * indent + '> ' )
                self.parsePara(child, outFile, 0, True)
            elif child.tag == 'programlisting':
                if firstItem:
                    raise Exception('programlisting as first child is not supported')
                self.parseProgramListing(child, outFile, 4, prefix='> ')
            else:
                raise Exception('Unsupported type: ' + child.tag)
            outFile.write('\n\n')
        outFile.write('\n')
            

    def parseChapter(self, node, outFile):
        for child in node.getchildren():
            if child.tag == 'title':
                title = self.getTitle(child)
                if len(title) == 0:
                    raise Exception('Invalid title')
                indent = 0
                if node.tag == 'chapter':
                    indent = 1
                elif node.tag == 'sect1' or node.tag == 'preface':
                    indent = 2
                elif node.tag == 'sect2':
                    indent = 3
                elif node.tag == 'sect3' or node.tag == 'refsect1':
                    indent = 4
                else:
                    raise Exception('Unsupported type: ' + node.tag)
                outFile.write('#' * indent + ' ' + title + '\n\n')
            elif child.tag == 'sect1':
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + '.md'
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('sec1: "' + fileName + '" is existing')
                outFile = open(fileName, 'w')
                self.parseChapter(child, outFile)
                outFile.close()
                simplifySpaces(fileName)
            elif child.tag == 'sect2' or child.tag == 'sect3' or child.tag == 'refentry' or child.tag == 'refsect1':
                self.parseChapter(child, outFile)
            elif child.tag == 'para':
                self.parsePara(child, outFile)
                outFile.write('\n\n')
            elif child.tag == 'table':
                self.parseTable(child, outFile)
            elif child.tag == 'programlisting':
                self.parseProgramListing(child, outFile)
            elif child.tag == 'figure':
                self.parseFigure(child, outFile)
            elif child.tag == 'itemizedlist':
                self.parseList(child, outFile, False)
            elif child.tag == 'orderedlist':
                self.parseList(child, outFile, True)
            elif child.tag == 'title':
                pass # ok: dealt in another way
            elif child.tag == 'procedure':
                raise Exception('Should be converted into an ordered item list in the script preprocessor: ' + child.tag)
            elif child.tag == 'note':
                self.parseIconPara(child, outFile)
            elif child.tag == 'handson':
                self.parseIconPara(child, outFile)
            elif child.tag == 'theory':
                self.parseIconPara(child, outFile)
            elif child.tag == 'code':
                subchildren = child.findall('./programlisting')
                if len(subchildren) != 1 and len(child.getchildren()) != 1:
                    raise Exception('Unexpected number of children for the <code> tag')
                self.parseProgramListing(subchildren[0], outFile)
            elif child.tag == 'clearPage':
                pass # TODO
            elif child.tag == 'keywords':
                pass # TODO
            elif child.tag == 'refnamediv':
                pass # TODO
            elif child.tag == 'refsynopsisdiv':
                pass # TODO
            elif child.tag == 'refmeta':
                pass # TODO
            else:
                raise Exception('Unsupported type: ' + child.tag)


    def parseBook(self, node, outFile):
        for child in node.getchildren():
            if child.tag == 'bookinfo':
                for subchild in child.getchildren():
                    if subchild.tag == 'title':
                        outFile.write('# ' + subchild.attrib.get('name', subchild.text) + '\n\n')
            elif child.tag == 'preface':
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + '.md'
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('preface: "' + fileName + '" is existing')
                outFile = open(fileName, 'w')
                self.parseChapter(child, outFile)
                outFile.close()
                simplifySpaces(fileName)
            elif child.tag == 'chapter':
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + '.md'
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('chapter: "' + fileName + '" is existing')
                outFile = open(fileName, 'w')
                self.parseChapter(child, outFile)
                outFile.close()
                simplifySpaces(fileName)
            else:
                raise Exception('Unsupported type: ' + child.tag)


if __name__ == '__main__':
    webotsDirectoryPath = '../webots/'
    documentationInputDirectoriesPaths = [webotsDirectoryPath + 'src/doc/guide/', webotsDirectoryPath + 'src/doc/reference/']

    for inputDirectoryPath in documentationInputDirectoriesPaths:
        directoryName = os.path.basename(os.path.dirname(inputDirectoryPath)) # guide or reference
        print 'Directory name: ' + directoryName

        intputFilePath = inputDirectoryPath + directoryName + '.xml'
        print 'Input file name: ' + intputFilePath

        bookParser = BookParser(webotsDirectoryPath, directoryName)
        bookParser.parseXMLFile(intputFilePath)
        bookParser.exportToc()
        bookParser.export()
