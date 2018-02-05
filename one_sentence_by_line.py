"""Refactor paragraphs to have one sentence by line."""
import glob
import shutil

pBuffer = ''


def flushBuffer(f):
    """Flush pBuffer :-P."""
    global pBuffer
    txt = pBuffer.replace('\n', ' ')
    txt = txt.replace('  ', ' ')
    txt = txt.replace('. ', '.\n')
    txt = txt.replace(' \n', '\n')
    txt += '\n'
    txt = txt.replace('\n\n', '\n')
    f.write(txt)
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

            if line.startswith('- ') and pBuffer:
                flushBuffer(f)

            if line.startswith('#') or line.startswith('---') or line.startswith('\n'):
                flushBuffer(f)
                f.write(line)
            elif line.startswith('%figure') or line.startswith('%api'):
                flushBuffer(f)
                skipUntil = '%end'
                f.write(line)
            elif line.startswith('| '):
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

    shutil.move(backup, filename)
