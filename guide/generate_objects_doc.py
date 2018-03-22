#!/usr/bin/env python

import fnmatch
import os
import re
import sys

DESCRIPTION_STATE = 0
FIELDS_STATE = 1
BODY_STATE = 2

categories = []
with open('objects.md', 'w') as file:
    file.write('# Objects\n\n')
    file.write('## Sections\n\n')

for rootPath, dirNames, fileNames in os.walk(os.environ['WEBOTS_HOME'] + os.sep + 'projects' + os.sep + 'objects'):
    for fileName in fnmatch.filter(fileNames, '*.proto'):
        proto = os.path.join(rootPath, fileName)
        protoName = os.path.basename(proto).split('.')[0]
        category = os.path.basename(os.path.dirname(os.path.dirname(proto)))
        categoryName = category.replace('_', '-')
        description = ''
        license = ''
        fields = ''
        state = 0
        describedField = []
        with open(proto, 'r') as file:
            for line in file.readlines():
                if state == DESCRIPTION_STATE:
                    if line.startswith('#'):
                        if line.startswith('#VRML_SIM') or line.startswith('# tags'):
                            continue
                        elif line.startswith('# license:'):
                            license = line.replace('# license:', '').strip()
                        else:
                            description += line.replace('#', '').strip() + '\n'
                    elif line.startswith('PROTO '):
                        state = FIELDS_STATE
                elif state == FIELDS_STATE:
                    if line.startswith(']'):
                        state = BODY_STATE
                    else:
                        match = re.match(r'.*ield\s+([^ ]*)\s+([^ ]*)\s+([^#]*)\s+#(.*)', line)
                        if match:
                            fieldType = match.group(1)
                            fieldName = match.group(2)
                            fieldDefaultValue = match.group(3)
                            fieldComment = match.group(4).strip()
                            describedField.append((fieldName, fieldComment))
                        fields += line.replace('vrmlField ', '').replace('field', '   ').split('#')[0]
                        if '#' in line:
                            fields += '\n'
        exist = os.path.isfile(categoryName + '.md')
        mode = 'a'
        if category not in categories:
            mode = 'w'
        with open(categoryName + '.md', mode) as file:
            if mode == 'w':
                file.write('# %s\n\n' % categoryName.replace('-', ' ').title())
            file.write('## %s\n\n' % protoName)

            if os.path.isfile('images' + os.sep + 'objects' + os.sep + category + os.sep + protoName + '/model.png'):
                file.write('%%figure "%s"\n\n' % protoName)
                file.write('![%s-image](images/objects/%s/%s/model.png)\n\n' % (protoName, category, protoName))
                file.write('%end\n\n')
            else:
                sys.stderr.write('Please add a "%s" file.\n' % ('images' + os.sep + 'objects' + os.sep + category + os.sep + protoName + '/model.png'))

            file.write('```\n')
            file.write('%s {\n' % protoName)
            file.write(fields)
            file.write('}\n')
            file.write('```\n\n')

            file.write('> **File location**: "WEBOTS\_HOME%s"\n\n' % proto.replace(os.environ['WEBOTS_HOME'], '').replace(os.sep, '/'))
            if license:
                file.write('> **License**: %s\n\n' % license)
            else:
                sys.stderr.write('Please add a license to "%s"\n' % proto)

            file.write('### Description\n\n')
            file.write(description + '\n')

            if describedField:
                file.write('### Field Summary\n\n')
                for fieldName, fieldDescription in describedField:
                    file.write('- `%s`: %s\n\n' % (fieldName, fieldDescription))

        if category not in categories:
            categories.append(category)

categories = sorted(categories)
with open('objects.md', 'a') as file:
    for category in categories:
        file.write('- [%s](%s.md)\n' % (category.replace('-', ' ').title(), category))
    file.write('\n')
