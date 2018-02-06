"""Refactor paragraphs to have one sentence by line."""
import glob
import os

pBuffer = ''


def flushBuffer(f):
    """Flush pBuffer :-P."""
    global pBuffer
    txt = pBuffer.replace('\n', ' ')
    txt = txt.replace('  ', ' ')
    txt = txt.replace('. ', '.\n')
    txt = txt.replace(' \n', '\n')
    txt = txt.strip()
    f.write(txt)
    f.write('\n')
    pBuffer = ''


for filename in glob.glob('*/*.md'):
    backup = filename.replace('.md', '.back')
    with open(filename, 'r') as f:
        content = f.readlines()
    with open(backup, 'w') as f:
        skipUntil = None
        pBuffer = ''
        for line in content:
            assert(not skipUntil or not pBuffer)
            if skipUntil:
                f.write(line)
                if line.startswith(skipUntil):
                    skipUntil = None
                continue

            if line.startswith('\n'):
                flushBuffer(f)
                f.write(line)
            elif line.startswith('#') or line.startswith('---'):
                flushBuffer(f)
                f.write(line)
            elif line.startswith('%figure') or line.startswith('%api'):
                flushBuffer(f)
                skipUntil = '%end'
                f.write(line)
            elif line.startswith('| ') or line.startswith('- '):
                flushBuffer(f)
                skipUntil = '\n'
                f.write(line)
            elif line.startswith('```') or line.startswith('> ```'):
                flushBuffer(f)
                skipUntil = '```'
                f.write(line)
            else:
                pBuffer += line
        flushBuffer(f)

    with open(backup, 'r') as f:
        content = f.readlines()
    with open(filename, 'w') as f:
        previousLine = ''
        for l in range(len(content)):
            line = content[l]

            if l == 0 or l == len(content) - 1:
                if line == '\n':
                    previousLine = line
                    continue

            if previousLine != '\n' or line != '\n':
                f.write(line)
            previousLine = line

    os.remove(backup)
