#!/usr/bin/env python

import os
import re

DESCRIPTION_STATE = 0
FIELDS_STATE = 1
BODY_STATE = 2

with open('objects_list.txt') as objectListFile:
    protoList = []
    for line in objectListFile.readlines():
        protoList.append(line.strip('\n'))
    protoList = sorted(protoList)
    addedCategory = []
    with open('objects.md', 'w') as file:
        file.write('# Objects\n\n')
        file.write('## Sections\n\n')

    for proto in protoList:
        protoName = os.path.basename(proto).split('.')[0]
        category = os.path.basename(os.path.dirname(os.path.dirname(proto)))
        categoryName = category.replace('_', '-')
        description = ''
        license = ''
        fields = ''
        state = 0
        describedField = []
        with open(os.environ['WEBOTS_HOME'] + os.sep + proto, 'r') as file:
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
                        fields += '  ' + line.replace('vrmlField', '').replace('field', '').split('#')[0].strip() + '\n'

        exist = os.path.isfile(categoryName + '.md')
        mode = 'a'
        if category not in addedCategory:
            mode = 'w'
        with open(categoryName + '.md', mode) as file:
            if mode == 'w':
                file.write('# %s\n\n' % categoryName.replace('-', ' ').title())
            file.write('## %s\n\n' % protoName)

            if os.path.isfile('images' + os.sep + category + os.sep + protoName + '/model.png'):
                file.write('%%figure "%s"\n\n' % protoName)
                file.write('![%s](images/%s/%s/model.png)\n\n' % (protoName, category, protoName))
                file.write('%end\n\n')
            else:
                print('Please add a "%s" file.' % ('images' + os.sep + category + os.sep + protoName + '/model.png'))

            file.write('```\n')
            file.write('%s {\n' % protoName)
            file.write(fields)
            file.write('}\n')
            file.write('```\n\n')

            file.write('### Description\n\n')
            file.write(description + '\n')

            if describedField:
                file.write('### Field Summary\n\n')
                for fieldName, fieldDescription in describedField:
                    file.write('- `%s`: %s\n\n' % (fieldName, fieldDescription))

            if license:
                file.write('> **Note** [License]: %s\n\n\n' % license)

        if category not in addedCategory:
            addedCategory.append(category)
            with open('objects.md', 'a') as file:
                file.write('- [%s](%s.md)\n' % (categoryName.replace('-', ' ').title(), categoryName))
    with open('objects.md', 'a') as file:
        file.write('\n')
