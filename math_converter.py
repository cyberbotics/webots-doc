#!/usr/bin/env python

"""Convert images to TEX formulas."""

import glob
import os
import re


def file_replace(file, pattern, subst):
    """Search and replace a regex into a file."""
    # Read contents from file as a single string
    file_handle = open(file, 'r')
    file_string = file_handle.read()
    file_handle.close()

    # Use RE package to allow for replacement (also allowing for (multiline) REGEX)
    file_string = (re.sub(pattern, subst, file_string))

    # Write contents to file.
    # Using mode 'w' truncates the file.
    file_handle = open(file, 'w')
    file_handle.write(file_string)
    file_handle.close()


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
            formula = formula.replace('\\', '\\\\')
            formula = re.sub(r'\s*[\r\n]', '\n', formula)
            formulas.append(formula)
            print '-> %s\n' % (formula)

        for mdFilePath in mdFilePaths:
            book = os.path.basename(os.path.dirname(mdFilePath))
            imagePath = 'images' + os.sep + name + '.png'
            imageCompletePath = book + os.sep + imagePath
            if os.path.exists(imageCompletePath):
                file_replace(mdFilePath, r'!\[.*\]\(%s\)\s' % (imagePath), formula + '\n')
