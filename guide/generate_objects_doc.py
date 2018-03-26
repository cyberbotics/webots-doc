#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fnmatch
import os
import re
import sys

# https://github.com/rcompton/ryancompton.net/blob/master/assets/praw_drugs/urlmarker.py
WEB_URL_REGEX = r"""(?i)\b((?:https?:(?:/{1,3}|[a-z0-9%])|[a-z0-9.\-]+[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)/)(?:[^\s()<>{}\[\]]+|\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\))+(?:\([^\s()]*?\([^\s()]+\)[^\s()]*?\)|\([^\s]+?\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’])|(?:(?<!@)[a-z0-9]+(?:[.\-][a-z0-9]+)*[.](?:com|net|org|edu|gov|mil|aero|asia|biz|cat|coop|info|int|jobs|mobi|museum|name|post|pro|tel|travel|xxx|ac|ad|ae|af|ag|ai|al|am|an|ao|aq|ar|as|at|au|aw|ax|az|ba|bb|bd|be|bf|bg|bh|bi|bj|bm|bn|bo|br|bs|bt|bv|bw|by|bz|ca|cc|cd|cf|cg|ch|ci|ck|cl|cm|cn|co|cr|cs|cu|cv|cx|cy|cz|dd|de|dj|dk|dm|do|dz|ec|ee|eg|eh|er|es|et|eu|fi|fj|fk|fm|fo|fr|ga|gb|gd|ge|gf|gg|gh|gi|gl|gm|gn|gp|gq|gr|gs|gt|gu|gw|gy|hk|hm|hn|hr|ht|hu|id|ie|il|im|in|io|iq|ir|is|it|je|jm|jo|jp|ke|kg|kh|ki|km|kn|kp|kr|kw|ky|kz|la|lb|lc|li|lk|lr|ls|lt|lu|lv|ly|ma|mc|md|me|mg|mh|mk|ml|mm|mn|mo|mp|mq|mr|ms|mt|mu|mv|mw|mx|my|mz|na|nc|ne|nf|ng|ni|nl|no|np|nr|nu|nz|om|pa|pe|pf|pg|ph|pk|pl|pm|pn|pr|ps|pt|pw|py|qa|re|ro|rs|ru|rw|sa|sb|sc|sd|se|sg|sh|si|sj|Ja|sk|sl|sm|sn|so|sr|ss|st|su|sv|sx|sy|sz|tc|td|tf|tg|th|tj|tk|tl|tm|tn|to|tp|tr|tt|tv|tw|tz|ua|ug|uk|us|uy|uz|va|vc|ve|vg|vi|vn|vu|wf|ws|ye|yt|yu|za|zm|zw)\b/?(?!@)))"""

DESCRIPTION_STATE = 0
FIELDS_STATE = 1
BODY_STATE = 2

fileList = []
upperCategories = {}
with open('objects.md', 'w') as file:
    file.write('# Objects\n\n')
    file.write('## Sections\n\n')

for rootPath, dirNames, fileNames in os.walk(os.environ['WEBOTS_HOME'] + os.sep + 'projects' + os.sep + 'objects'):
    for fileName in fnmatch.filter(fileNames, '*.proto'):
        fileList.append(os.path.join(rootPath, fileName))

fileList = sorted(fileList)
for proto in fileList:
    protoName = os.path.basename(proto).split('.')[0]
    category = os.path.basename(os.path.dirname(os.path.dirname(proto)))
    upperCategory = os.path.basename(os.path.dirname(os.path.dirname(os.path.dirname(proto))))
    if upperCategory == 'objects':
        upperCategory = category
    upperCategoryName = upperCategory.replace('_', '-')
    description = ''
    license = ''
    licenseUrl = ''
    fields = ''
    state = 0
    describedField = []
    with open(proto, 'r') as file:
        skipProto = False
        closingAccolades = 0
        for line in file.readlines():
            closingAccolades += line.count(']') - line.count('[')
            if state == DESCRIPTION_STATE:
                if line.startswith('#'):
                    if line.startswith('#VRML_SIM'):
                        continue
                    elif line.startswith('# license:'):
                        license = line.replace('# license:', '').strip()
                    elif line.startswith('# license url:'):
                        licenseUrl = line.replace('# license url:', '').strip()
                    elif line.startswith('# tags:'):
                        if 'deprecated' in line or 'hidden' in line:
                            skipProto = True
                            break
                    else:
                        newLine = line.replace('#', '').replace('_', '\_').strip()
                        urls = re.findall(WEB_URL_REGEX, newLine)
                        for url in urls:
                            newLine = newLine.replace(url, '[%s](%s)' % (url, url))
                        description += newLine + '\n'
                elif line.startswith('PROTO '):
                    state = FIELDS_STATE
            elif state == FIELDS_STATE:
                if closingAccolades >= 0:
                    state = BODY_STATE
                else:
                    match = re.match(r'.*ield\s+([^ ]*)\s+([^ ]*)\s+([^#]*)\s+#(.*)', line)
                    if match and match.group(1) != 'hiddenField':
                        fieldType = match.group(1)
                        fieldName = match.group(2)
                        fieldDefaultValue = match.group(3)
                        fieldComment = match.group(4).strip()
                        describedField.append((fieldName, fieldComment))
                    fieldLine = line.replace('field ', '').split('#')[0]
                    if 'hiddenField' not in fieldLine:
                        fields += fieldLine
                        if '#' in line:
                            fields += '\n'
    if skipProto:
        continue
    exist = os.path.isfile('object-' + upperCategoryName + '.md')
    mode = 'a'
    if upperCategory not in upperCategories:
        mode = 'w'
    with open('object-' + upperCategoryName + '.md', mode) as file:
        if upperCategory not in upperCategories or category not in upperCategories[upperCategory]:
            file.write('# %s\n\n' % category.replace('_', ' ').title())
        file.write('## %s\n\n' % protoName)

        if os.path.isfile('images' + os.sep + 'objects' + os.sep + category + os.sep + protoName + '/model.png'):
            file.write('%%figure "%s model in Webots."\n\n' % protoName)
            file.write('![%s](images/objects/%s/%s/model.png)\n\n' % (protoName, category, protoName))
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
            file.write('> **License**: %s\n' % license)
            if licenseUrl:
                file.write('[More information.](%s)\n' % licenseUrl)
            file.write('\n')
        # else:
        #     sys.stderr.write('Please add a license to "%s"\n' % proto)

        file.write('### %s Description\n\n' % protoName)
        file.write(description + '\n')

        if describedField:
            file.write('### %s Field Summary\n\n' % protoName)
            for fieldName, fieldDescription in describedField:
                file.write('- `%s`: %s\n\n' % (fieldName, fieldDescription))

    if upperCategory not in upperCategories:
        upperCategories[upperCategory] = []
        upperCategories[upperCategory].append(category)
    elif category not in upperCategories[upperCategory]:
        upperCategories[upperCategory].append(category)

upperCategoriesList = sorted(upperCategories.keys())
categoriesList = []
with open('objects.md', 'a') as file:
    for upperCategory in upperCategoriesList:
        categories = sorted(upperCategories[upperCategory])
        if not upperCategory == categories[0]:
            file.write('- [%s](object-%s.md)\n' % (upperCategory.replace('_', ' ').title(), upperCategory.replace('_', '-')))
        for category in categories:
            categoriesList.append(category)
            if upperCategory == category:
                file.write('- [%s](object-%s.md)\n' % (category.replace('_', ' ').title(), category.replace('_', '-')))
            else:
                file.write('  - [%s](object-%s.md#%s)\n' % (category.replace('_', ' ').title(), upperCategory.replace('_', '-'), category.replace('_', '-')))
    file.write('\n')
categoriesList = sorted(categoriesList)
print("Please update the 'Objects' part in 'menu.md' with:")
for category in upperCategoriesList:
    print('    - [%s](object-%s.md)' % (category.replace('_', ' ').title(), category.replace('_', '-')))
