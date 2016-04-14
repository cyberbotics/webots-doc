#!/usr/bin/env python

"""Convert images to TEX formulas."""

import glob
import os
import re


def file_replace(fname, pat, s_after):
    """Search and replace a regex into a file."""
    # first, see if the pattern is even in the file.
    with open(fname) as f:
        if not any(re.search(pat, line) for line in f):
            return  # pattern does not occur in file so we are done.

    # pattern is in the file, so perform replace operation.
    with open(fname) as f:
        out_fname = fname + ".tmp"
        out = open(out_fname, "w")
        for line in f:
            out.write(re.sub(pat, s_after, line))
        out.close()
        os.rename(out_fname, fname)


if __name__ == '__main__':
    formulasPath = '../webots/src/doc/formulas/'
    texFilepaths = []
    for filename in os.listdir(formulasPath):
        if filename.endswith('.tex'):
            texFilepaths.append(os.path.join(formulasPath, filename))
    mdFilePaths = glob.glob('*' + os.sep + '*.md')
    for texFilepath in texFilepaths:
        name = os.path.splitext(os.path.basename(texFilepath))[0]
        print name + ':'

        with open(texFilepath, 'r') as texFile:
            texContent = texFile.read()

        formulas = []

        for match in re.finditer(r'(\$\$[^\$]*\$\$)', texContent):
            formula = match.group(1)
            formulas.append(formula)
            print '-> %s\n' % (formula)

        for mdFilePath in mdFilePaths:
            book = os.path.basename(os.path.dirname(mdFilePath))
            imagePath = 'images' + os.sep + name + '.png'
            imageCompletePath = book + os.sep + imagePath
            if os.path.exists(imageCompletePath):
                file_replace(mdFilePath, r'!\[.*\]\(%s\)\s' % (imagePath), formula)
