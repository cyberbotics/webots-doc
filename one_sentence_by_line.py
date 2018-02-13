"""Refactor paragraphs to have one sentence by line."""
import glob
import os
import re

pBuffer = None


def flushBuffer(f):
    """Flush pBuffer :-P."""
    global pBuffer
    if pBuffer is None:
        return
    txt = pBuffer
    txt = txt.replace('\n', ' ')
    txt = txt.replace('i.e.', 'i@e@')
    txt = txt.replace('etc.', 'etc@')
    txt = txt.replace('e.g.', 'e@g@')
    txt = txt.replace('  ', ' ')
    txt = txt.replace('. ', '.\n')
    txt = txt.replace(' \n', '\n')
    txt = txt.replace('i@e@', 'i.e.')
    txt = txt.replace('etc@', 'etc.')
    txt = txt.replace('e@g@', 'e.g.')
    txt = txt.replace(' - ', '\n- ')
    txt = re.sub(r'^(\d)\.\n', r'\1. ', txt)
    txt = re.sub(r'\n(\d)\.\n', r'\n\1. ', txt)
    txt = txt.rstrip()
    f.write(txt)
    f.write('\n')
    pBuffer = None


for filename in glob.glob('*/*.md'):
    if filename.endswith('menu.md'):
        continue
    backup = filename.replace('.md', '.back')
    with open(filename, 'r') as f:
        content = f.readlines()
    with open(backup, 'w') as f:
        pBuffer = None
        skipUntil = None
        for line in content:
            assert(not skipUntil or not pBuffer)
            if skipUntil:
                f.write(line)
                if line.startswith(skipUntil):
                    skipUntil = None
                continue

            if pBuffer:
                if line.strip():
                    pBuffer += line
                else:
                    flushBuffer(f)
                    f.write(line)
                continue

            if line.startswith('```'):
                flushBuffer(f)
                skipUntil = '```'
                f.write(line)
            elif line.startswith('> ```'):
                flushBuffer(f)
                skipUntil = '> ```'
                f.write(line)
            elif line.startswith('- ') or re.match(r'^\d+\.\s', line):
                if pBuffer is None:
                    pBuffer = ''
                pBuffer += line
            else:
                flushBuffer(f)
                f.write(line)
        flushBuffer(f)

    with open(backup, 'r') as f:
        content = f.readlines()
    with open(filename, 'w') as f:
        previousLine = ''
        for l in range(len(content)):
            line = content[l]
            line = re.sub(r'\s*\n', '\n', line)

            if l == 0 or l == len(content) - 1:
                if line == '\n':
                    previousLine = line
                    continue

            if previousLine != '\n' or line != '\n':
                f.write(line)
            previousLine = line

    os.remove(backup)
