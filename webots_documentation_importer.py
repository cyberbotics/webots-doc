#!/usr/bin/env python

import glob
import os
import re
import shutil
import textwrap
import xml.etree.ElementTree as ET
import pdb # break with pdb.set_trace()


def remove_tags(text):
    return re.sub(r'<[^>]+>', '', text)

def slugify(txt):
  output = txt.lower()
  output = remove_tags(output)
  output = output.replace('+', 'p')
  output = re.sub(r'[\(\):`]', '', output)
  output = re.sub(r'\W+', '-', output)
  output = re.sub(r'^-*', '', output)
  output = re.sub(r'-*$', '', output)
  return output.strip(' ').strip('-')

def simplifySpaces(filename):
    with open(filename, 'r') as file:
        content = file.read()

    content = re.sub(r'[ \t]*\n', '\n', content)
    content = re.sub(r'\n\n\n*', '\n\n', content)

    outFile = open(filename, 'w')
    outFile.write(content)
    outFile.close()

class Reference:
    refId = ''
    filename = ''
    anchor=''
    kind=''

    def __init__(self, refId, filename='', anchor='', kind=''):
        if not refId or len(refId) <= 0:
            raise Exception('Invalid reference refId')
        self.refId = refId
        self.filename = filename
        self.anchor = anchor
        self.kind = kind

    def getKind(self, preceedingText):
        processedText = preceedingText.strip().lower()
        if len(processedText) > 0:
            lastWord = processedText.rsplit(None, 1)[-1]
            if lastWord.startswith('th'):
                return self.kind
            else:
                return 'this ' + self.kind
        else:
            return self.kind

    def getUrl(self):
        if len(self.anchor) > 0: 
            return '%s#%s' % (self.filename, self.anchor)
        else:
            return self.filename

    def __str__(self):
        if len(self.anchor) > 0: 
            return '%s: "%s#%s" (%s)' % (self.refId, self.filename, self.anchor, self.kind)
        else:
            return '%s: "%s" (%s)' % (self.refId, self.filename, self.kind)


class ReferenceManager:
    def __init__(self):
        self.refs = []

    def addReference(self, ref):
        if ref.__class__.__name__ == 'Reference':
            if self.getReferenceById(ref.refId) is not None:
                raise Exception('Duplicated refIds: ' + ref.refId)
            self.refs.append(ref)
        else:
            raise Exception('ReferenceManager accepts only References')

    def getReferenceById(self, refId):
        for ref in self.refs:
            if ref.refId == refId:
                return ref
        return None

    def __str__(self):
        text = 'References:\n'
        for ref in self.refs:
            text += ' - %s\n' % (ref)
        return text


class BookParser:
    def __init__(self, webotsDirectoryPath, bookName):
        self.bookName = bookName
        self.root = None
        
        self.outputDirectoryPath = self.bookName + '/'

        self.referenceManager = ReferenceManager()

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

        content = re.sub(r'&webots_(\w*)_version;', r'{{ webots.version.\1 }}', content)
        content = re.sub(r'&webots_kros_(\w*)_version;', r'{{ kros.version.\1 }}', content)

        # dealt with `procedure` and `step` nodes
        content = content.replace('<procedure>', '<orderedlist>') \
                         .replace('</procedure>', '</orderedlist>') \
                         .replace('<step>', '<listitem>') \
                         .replace('</step>', '</listitem>')

        self.root = ET.fromstring(content)
        self.parents = dict((c, p) for p in self.root.getiterator() for c in p)

    def exportMenu(self):
        if self.root is None:
            raise Exception('Cannot export menu')

        outputFilePath = self.outputDirectoryPath + 'menu.md'
        print 'Generating menu: ' + outputFilePath

        outFile = open(outputFilePath, 'w')

        chapterCounter = 0
        for chapterNode in self.root.findall('.//preface') + self.root.findall('.//chapter'):
            chapterCounter += 1
            title = self.getTitle(chapterNode)
            outFile.write('- [%s](%s)\n' % (title, slugify(title) + '.md'))
            sectionCounter = 0
            for sectionNode in chapterNode.findall('.//sect1'):
                sectionCounter += 1
                title = self.getTitle(sectionNode)
                outFile.write('    - [%s](%s)\n' % (title, slugify(title) + '.md'))
        outFile.close()
        simplifySpaces(outputFilePath)

    def parseReferences(self):
        for idNode in self.root.findall('.//*[@id]'):
            refId = idNode.attrib.get('id')
            anchor = ''
            if idNode.tag == 'refentry' or \
              (idNode.tag == 'table' and self.parents[idNode].tag == 'sect1'):
                anchor = slugify(refId)
            else:
                anchor = slugify(self.getTitle(idNode))

            filename = ''
            node = idNode
            while node is not None and node.tag != 'chapter' and node.tag != 'sect1':
                if node in self.parents:
                    node = self.parents[node]
                else:
                    node = None
                    break
            if node is not None:
                filename = slugify(self.getTitle(node)) + '.md'

            kind = ''
            if idNode.tag == 'sect1' or idNode.tag == 'sect2' or idNode.tag == 'sect3' or idNode.tag == 'preface' or idNode.tag == 'refentry':
                kind = 'section'
            else:
                kind = idNode.tag

            ref = Reference(refId, filename, anchor, kind)
            self.referenceManager.addReference(ref)

        print self.referenceManager


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
            titleNodes = node.findall('.//title')
            if len(titleNodes) <= 0:
                return ''
            title = titleNodes[0]

        text = ''
        if title.text:
            text += title.text
        for child in title.getchildren():
            if child.text:
                if child.tag == 'trademark':
                    text += '*' + child.text + '*<sup>TM</sup>'
                elif child.tag == 'function' or child.tag == 'math':
                    text += self.parseMath(child)
                else:
                    raise Exception('Unsupported type: ' + child.tag)
            if child.tail:
                text += child.tail
        text = text.strip()
        text = re.sub(r'\n', '', text)
        text = re.sub(r'  *', ' ', text)

        return text

    def parseText(self, txt, protectUnderScores, protectAngleBracket, removeTrailingSpaces):
        if txt is None:
            return ''
        output = txt.encode('utf-8')

        m = re.search(r'\&\w*;', output)
        if m:
          print m.group(0)

        if protectUnderScores:
            output = output.replace('_', '\\_')

        if protectAngleBracket:
            output = output.replace('<', '`<`')
            output = output.replace('>', '`>`')

        if removeTrailingSpaces:
            output = re.sub(r'[ \t]*\n', '\n', output)
            output = re.sub(r'[ \t]*$', '', output)
            output = re.sub(r'\n*$', '', output)
        return output

    def formatText(self, text):
        text.strip()
        content = text.split('\n')
        text = ' '.join(map(lambda x: x.strip(), content)).strip()
        content = textwrap.wrap(text, width=80, break_long_words=False, break_on_hyphens=False)
        output = ''
        for i in range(0, len(content)):
            line = content[i]
            output += line.strip()
            if i != len(content) - 1:
                output += '\n'
        return output

    def parsePara(self, node, outFile, indent=0, inList=False, mergeCarriageReturns=False, format=True):
        # para included tags:
        #     bold, command, computeroutput, email, emphasis, filename, function,
        #     guibutton, guilabel, guimenu, guimenuitem, guisubmenu, hlink,
        #     inlinegraphic, keycap, math, parameter, programlisting, trademark
        #     ulink, xref
        text = ''
        if node.text:
            text += self.parseText(node.text, True, mergeCarriageReturns, False)
        for child in node.getchildren():
            if child.text:
                if child.tag == 'bold':
                    text += '**' + self.parseText(child.text, True, False, False) + '**'
                elif child.tag == 'email':
                    text += '[' + self.parseText(child.text, True, False, False) + '](mailto:' + self.parseText(child.text, True, False, False) + ')'
                elif child.tag == 'emphasis':
                    text += '*' + self.parseText(child.text, True, False, False) + '*'
                elif child.tag == 'filename':
                    text += '"' + self.parseText(child.text, True, False, False) + '"'
                elif child.tag == 'math':
                    text += self.parseMath(child)
                elif child.tag == 'trademark':
                    text += '*' + self.parseText(child.text, True, False, False) + '*<sup>TM</sup>'
                elif child.tag == 'ulink':
                    text += '[' + self.parseText(child.text, True, False, False) + '](' + child.attrib.get('url') + ')'
                elif child.tag == 'xref':
                    linkend = child.attrib.get('linkend')
                    if linkend is None:
                        raise Exception('xref without linkend attribute')
                    ref = self.referenceManager.getReferenceById(linkend)
                    if ref is None:
                        raise Exception('reference to "' + linkend + '" is undefined')
                    text += '[%s](%s)' % (self.parseText(child.text, True, False, False), ref.getUrl())
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
                    text += '`' + self.parseText(child.text, False, False, False) + '`'
            else: # not a text tag
                if child.tag == 'space':
                    text += '&nbsp;'
                elif child.tag == 'inlinegraphic':
                    text += '![](' + child.attrib.get('fileref')
                    if child.attrib.get('width'):
                        text += ' ='
                        if child.attrib.get('width'):
                            text += child.attrib.get('width')
                        text += 'x'
                        if child.attrib.get('height'):
                            text += child.attrib.get('height')
                        else:
                            text += child.attrib.get('width')
                    text += ')'
                elif child.tag == 'xref':
                    linkend = child.attrib.get('linkend')
                    if linkend is None:
                        raise Exception('xref without linkend attribute')
                    ref = self.referenceManager.getReferenceById(linkend)
                    if ref is None:
                        raise Exception('reference to "' + linkend + '" is undefined')
                    text += '[%s](%s)' % (ref.getKind(text), ref.getUrl())
            text += self.parseText(child.tail, True, mergeCarriageReturns, False)

        if mergeCarriageReturns:
            text = re.sub(r'\n', ' ', text)
            text = re.sub(r'[ \t]+', ' ', text)

        if format:
            text = self.formatText(text)

            content = text.split('\n')
            for i in range(0, len(content)):
                line = content[i]
                if len(line.strip()) > 0:
                    outFile.write(' ' * indent + line)
                if i != len(content) - 1:
                    outFile.write('\n')
        else:
            outFile.write(text.strip())

    def parseMath(self, node):
        text = '*' + self.readRawText(node, True).strip().encode('utf-8') + '*'
        text = re.sub(r'\n', ' ', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text

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

        text = self.parseText(node.text, False, False, True)
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
            outFile.write('\n%%figure "%s"\n\n![%s](%s)\n\n%%end\n\n' % (title, title, fileref))

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
            outFile.write('%%figure "%s"\n\n' % (title))

        # exception: display the anchor
        if nCols == 1 and node.attrib.get('id') and \
           (node.attrib.get('id').startswith('cpp_') or node.attrib.get('id').startswith('java_') or \
            node.attrib.get('id').startswith('python_') or node.attrib.get('id').startswith('matlab_')):
            outFile.write('<a name="%s"/>\n\n' % (node.attrib.get('id')))

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
                self.parsePara(entryNode, outFile, mergeCarriageReturns=True, format=False)
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
            outFile.write('\n%end\n\n')

        outFile.write('\n')

    def parseIconPara(self, node, outFile, indent=0):
        outFile.write(' ' * indent + '> **' + node.tag + '**')

        languageTags = {'c': 'C', 'C': 'C++', 'J': 'Java', 'm': 'Matlab', 'M': 'Matlab', 'P': 'Python', 'R': 'Ros'}
        lang = node.attrib.get('lang')
        if lang:
            outFile.write(' [')
            firstLang = True
            for l in lang:
                if firstLang:
                    firstLang = False
                else:
                    outFile.write(', ')
                outFile.write(languageTags[l])
                
            outFile.write(']')
        outFile.write(': ')

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

    def readRawText(self, node, keepTags=False):
        text = ''
        if node.text:
            text += node.text;
        for child in node.getchildren():
            if keepTags:
                text += '<' + child.tag + '>'
            text += self.readRawText(child)
            if keepTags:
                text += '</' + child.tag + '>'
        return text

    def parseFuncPrototype(self, node, outFile):
        firstParamDef = True
        funcdefCounter = 0
        for child in node.getchildren():
            if child.tag == 'funcdef':
                funcdefCounter += 1
                outFile.write(self.readRawText(child).strip() + '(')
            elif child.tag == 'paramdef':
                if firstParamDef:
                    firstParamDef = False
                else:
                    outFile.write(', ')
                outFile.write(self.readRawText(child).strip())
            else:
                raise Exception('Unsupported node ' + child.tag)
        outFile.write(')\n')
        if funcdefCounter != 1:
            raise Exception('Bad number of funcded nodes: ' + funcdefCounter)

    def parseRefEntry(self, node, outFile):
        languageTags = [
            ('cpp_id', 'C++'),
            ('java_id', 'Java'),
            ('python_id', 'Python'),
            ('matlab_id', 'Matlab'),
            ('ros_id', 'ROS')
        ]
        for child in node.getchildren():
            if child.tag == 'refnamediv':
                indent = 4
                anchorRef = ''
                if node.attrib.get('id'):
                    anchorRef = '<a name="' + slugify(node.attrib.get('id')) + '"/>'
                outFile.write('#' * indent + ' ' + anchorRef + 'Name\n\n')
                firstRefName = True
                for subchild in node.findall('.//refname'):
                    if firstRefName:
                        firstRefName = False
                    else:
                        outFile.write(', ')
                    outFile.write('**' + self.parseText(subchild.text, True, False, False).strip() + '**')
                for subchild in node.findall('.//refpurpose'):
                    outFile.write(' - *' + self.parseText(subchild.text, True, False, False).strip() + '*\n\n')
            elif child.tag == 'refsynopsisdiv':
                firstTag = True
                for (tag, tagName) in languageTags:
                    tagValue = child.attrib.get(tag)
                    if tagValue and len(tagValue) > 0:
                        ref = self.referenceManager.getReferenceById(tagValue)
                        if ref:
                            # print tagValue, ref
                            if firstTag:
                                firstTag = False
                            else:
                                outFile.write(', ')
                            outFile.write('{[%s](%s)}' % (tagName, ref.getUrl()))
                if not firstTag:
                    outFile.write('\n\n')

                funcsynopsis = child.findall('./funcsynopsis')
                if len(funcsynopsis) != 1:
                    raise Exception("1 funcsynopsis expected")
                funcsynopsis = funcsynopsis[0]

                outFile.write('``` c\n')
                for subchild in funcsynopsis.getchildren():
                    if subchild.tag == 'funcsynopsisinfo':
                        outFile.write(subchild.text.strip() + '\n\n')
                    elif subchild.tag == 'funcprototype':
                        self.parseFuncPrototype(subchild, outFile)
                    else:
                        raise Exception('Unsupported node ' + subchild.tag)
                outFile.write('```\n\n')
            elif child.tag == 'refsect1':
                self.parseChapter(child, outFile)

    def parseKeywords(self, node, outFile):
        outFile.write('**Keywords**: ' + self.readRawText(node).strip() + '\n')

    def parseChapter(self, node, outFile):
        firstRefEntry = True
        previousChildTag = 'Ni'
        for child in node.getchildren():
            if child.tag == 'title':
                title = self.getTitle(child)
                if len(title) == 0:
                    raise Exception('Invalid title')
                indent = 0
                if node.tag == 'chapter':
                    indent = 1
                elif node.tag == 'sect1' or node.tag == 'preface' or node.tag == 'legalnotice':
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
                newOutFile = open(fileName, 'w')
                self.parseChapter(child, newOutFile)
                newOutFile.close()
                simplifySpaces(fileName)
            elif child.tag == 'sect2' or child.tag == 'sect3' or child.tag == 'refsect1':
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
            elif child.tag == 'note' or child.tag == 'handson' or child.tag == 'theory':
                if previousChildTag == 'note' or previousChildTag == 'handson' or previousChildTag == 'theory':
                    # cf: http://stackoverflow.com/questions/12979577/how-can-i-write-two-separate-blockquotes-in-sequence-using-markdown
                    outFile.write('<!-- -->\n\n')
                self.parseIconPara(child, outFile)
            elif child.tag == 'code':
                subchildren = child.findall('./programlisting')
                if len(subchildren) != 1 and len(child.getchildren()) != 1:
                    raise Exception('Unexpected number of children for the <code> tag')
                self.parseProgramListing(subchildren[0], outFile)
            elif child.tag == 'clearPage':
                pass # no sense in the new implementation
            elif child.tag == 'keywords':
                self.parseKeywords(child, outFile)
            elif child.tag == 'refentry':
                if firstRefEntry:
                    firstRefEntry = False
                else:
                    outFile.write('---\n\n')
                self.parseRefEntry(child, outFile)
            else:
                raise Exception('Unsupported type: ' + child.tag)
            previousChildTag = child.tag

        if node.tag == 'chapter':
            outFile.write('## Sections\n')
            for child in node.getchildren():
                if child.tag == 'sect1':
                    title = self.getTitle(child)
                    fileName = slugify(title) + '.md'
                    outFile.write('- [%s](%s)\n' % (title, fileName))


    def parseBookInfo(self, node, outFile):
        for child in node.getchildren():
            if child.tag == 'edition':
                outFile.write('Release ' + child.text + '\n\n')
            elif child.tag == 'title':
                pass
            elif child.tag == 'mediaobject':
                imagedata = child.findall('.//imagedata')[0]
                fileref = imagedata.attrib.get('fileref')
                fileref = fileref.replace('1234.png', '1234web.png') # hack the path
                outFile.write('%%figure\n![%s](%s)\n%%end\n\n' % ('ImageData', fileref))
            elif child.tag == 'author':
                pass # no more sense in my opinion
            elif child.tag == 'publisher':
                text = self.readRawText(child).strip()
                text = re.sub(r'\n *', '\n', text)
                outFile.write(text + '\n\n')
            elif child.tag == 'releaseinfo':
                outFile.write(self.readRawText(child).strip() + '\n\n')
            elif child.tag == 'copyright':
                outFile.write('Copyright &copy; {{ date.year }}: ')
                outFile.write(self.readRawText(child).strip() + '\n\n')
            elif child.tag == 'legalnotice':
                self.parseChapter(child, outFile)
            else: # TODO: uncomment this
                raise Exception('Unsupported node: ' + child.tag)

    def parseBook(self, node, outFile):
        outFile.write('# ' + self.getTitle(node) + '\n\n')
        for child in node.getchildren():
            if child.tag == 'bookinfo':
                self.parseBookInfo(child, outFile)
            elif child.tag == 'preface':
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + '.md'
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('preface: "' + fileName + '" is existing')
                newOutFile = open(fileName, 'w')
                self.parseChapter(child, newOutFile)
                newOutFile.close()
                simplifySpaces(fileName)
            elif child.tag == 'chapter':
                fileName = self.outputDirectoryPath + slugify(self.getTitle(child)) + '.md'
                print 'Generating ' + fileName
                if os.path.exists(fileName):
                    raise Exception('chapter: "' + fileName + '" is existing')
                newOutFile = open(fileName, 'w')
                self.parseChapter(child, newOutFile)
                newOutFile.close()
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
        bookParser.exportMenu()
        bookParser.parseReferences()
        bookParser.export()
