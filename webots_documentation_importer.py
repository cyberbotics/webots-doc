#!/usr/bin/env python

import glob
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

    def export(self):
        if self.root is None:
            raise Exception('Cannot export book')

        outputFilePath = self.outputDirectoryPath + self.bookName + '.md'
        print 'Generating file: ' + outputFilePath
        outFile = open(outputFilePath, 'w')
        self.parseBook(self.root, outFile)
        outFile.close()

    def getTitle(self, el):
      titleNodes = el.findall('title')
      if len(titleNodes) <= 0:
          raise Exception('Cannot find title')
      return titleNodes[0].text.strip()

    def parseText(self, txt):
        if txt is None:
            return ''
        return txt.encode('utf-8')

    def parsePara(self, node, outFile, format):
        # para included tags:
        #     bold, command, computeroutput, email, emphasis, filename, function,
        #     guibutton, guilabel, guimenu, guimenuitem, guisubmenu, hlink,
        #     inlinegraphic, keycap, math, parameter, programlisting, trademark
        #     ulink, xref
        text = ''
        containsProgram = False
        if node.text:
            text += self.parseText(node.text)
        for child in node.getchildren():
            if child.text:
                if child.tag == 'bold':
                    text += '**' + self.parseText(child.text) + '**'
                elif child.tag == 'emphasis':
                    text += '*' + self.parseText(child.text) + '*'
                elif child.tag == 'filename':
                    text += '"' + self.parseText(child.text) + '"'
                elif child.tag == 'ulink':
                    text += '[' + self.parseText(child.text) + '](' + child.attrib.get('url') + ')'
                elif child.tag == 'programlisting':
                    text += self.parseProgramListing(child, None)
                    text = re.sub(r"(\s)*$", "\n", text)
                    containsProgram = True
                else:
                    text += '`' + self.parseText(child.text) + '`'
            text += self.parseText(child.tail)
        text += self.parseText(node.tail)

        if containsProgram:
            content = text.split('\n')
            inProgram = False
            for line in content:
                if '```' in line:
                    inProgram = not inProgram
                
                if inProgram:
                    line = re.sub(r"(\s)*$", "", line)
                    outFile.write(line + '\n')
                else:
                    outFile.write(line.strip() + '\n')
        elif format:
            content = text.split('\n')
            text = ' '.join(map(lambda x: x.strip(), content)).strip()
            content = textwrap.wrap(text, width=80)
            for line in content:
                outFile.write(line.strip() + '\n')
            outFile.write('\n')
        else:
            text = text.replace('\n', ' ')
            while '  ' in text:
                text = text.replace('  ', ' ')
            outFile.write(text.strip())

    def parseProgramListing(self, node, outFile):
        output = '\n```'
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
        output += self.parseText(node.text) + '\n'
        output += '```\n\n'

        if outFile:
            outFile.write(output)
        else:
            return output

    def parseFigure(self, node, outFile):
        title = ''
        fileref = ''
        for child in node.getchildren():
            if child.tag == 'title':
                title = child.text.strip()
            elif child.tag  == 'graphic':
                fileref = child.attrib.get('fileref')
            else:
                raise Exception('Unsupported type: ' + child.tag)
        if title is not None and len(title) > 0 and fileref is not None and len(fileref) > 0:
            if fileref.endswith('.pdf'):
                fileref += '.png'
            outFile.write('\n%%figure "%s"\n![%s](%s)\n%%end\n\n' % (title, title, fileref))

    def parseList(self, node, outFile, ordered):
        items = node.findall('./listitem')
        counter = 0
        for item in items:
            counter = counter + 1
            if ordered:
                outFile.write('%d. ' % (counter,))
            else:
                outFile.write('- ')
            for child in item.getchildren():
                if child.tag == 'para':
                    self.parsePara(child, outFile, False)
                elif child.tag == 'figure':
                    outFile.write('\n\n')
                    self.parseFigure(child, outFile)
                elif child.tag == 'note':
                    pass # TODO
                elif child.tag == 'programlisting':
                    pass # TODO
                else:
                    raise Exception('Unsupported type: ' + child.tag)
            outFile.write('\n')
        outFile.write('\n')

    def parseTable(self, node, outFile):
        header = len(node.findall('.//thead')) == 1
        nCols = int(node.findall('tgroup')[0].attrib.get('cols'))

        if not header and nCols == 1:
            outFile.write('```')

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
                self.parsePara(entryNode, outFile, False)
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

        if not header and nCols == 1:
            outFile.write('```')

        outFile.write('\n')

    def parseChapter(self, node, outFile):
        for child in node.getchildren():
            if child.tag == 'title' and child.attrib.get('name', child.text):
                indent = 0
                if node.tag == 'chapter':
                    indent = 1
                elif node.tag == 'sect1' or node.tag == 'preface':
                    indent = 2
                elif node.tag == 'sect2':
                    indent = 3
                elif node.tag == 'sect3':
                    indent = 4
                else:
                    raise Exception('Unsupported type: ' + node.tag)
                outFile.write('#' * indent + ' ' + child.attrib.get('name', child.text) + '\n\n')
            elif child.tag == 'sect1':
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + ".md"
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('sec1: "' + fileName + '" is existing')
                outFile = open(fileName, 'w')
                self.parseChapter(child, outFile)
                outFile.close()
            elif child.tag == 'sect2' or child.tag == 'sect3':
                self.parseChapter(child, outFile)
            elif child.tag == 'para':
                self.parsePara(child, outFile, True)
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
                pass # TODO
            elif child.tag == 'note':
                pass # TODO
            elif child.tag == 'handson':
                pass # TODO
            elif child.tag == 'theory':
                pass # TODO
            elif child.tag == 'refentry':
                pass # TODO
            elif child.tag == 'code':
                pass # TODO
            elif child.tag == 'clearPage':
                pass # TODO
            elif child.tag == 'keywords':
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
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + ".md"
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('preface: "' + fileName + '" is existing')
                outFile = open(fileName, 'w')
                self.parseChapter(child, outFile)
                outFile.close()
            elif child.tag == 'chapter':
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + ".md"
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('chapter: "' + fileName + '" is existing')
                outFile = open(fileName, 'w')
                self.parseChapter(child, outFile)
                outFile.close()
            else:
                raise Exception('Unsupported type: ' + child.tag)


if __name__ == "__main__":
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
