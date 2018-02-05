"""Refactor paragraphs to have one sentence by line."""
import glob

path = "*/*.md"

for filename in glob.glob(path):
    backup = filename.replace('.md', '.backup.md')
    with open(filename, 'r') as f:
        content = f.readlines()
    with open(backup, 'w') as f:
        skipUntil = None
        for line in content:
            if skipUntil:
                f.write(line)
                if line.startswith(skipUntil):
                    skipUntil = None
                continue

            if line.startswith('#'):
                f.write(line)
            elif line.startswith('%figure') or line.startswith('%api'):
                skipUntil = '%end'
                f.write(line)
            elif line.startswith('| '):
                skipUntil = '\n'
                f.write(line)
            elif line.startswith('```'):
                skipUntil = '```'
                f.write(line)
            else:
                print line[:-1]
