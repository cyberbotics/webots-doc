"""Extract MD from fields.txt."""
# Generate "robots.txt": 'find projects/robots -name *.proto' + manual cleanup
# Generate "fields.txt": 'cat robots.txt | xargs head -60 | grep "proto\|field" > fields.txt' + manual cleanup

import os
import re

with open('fields.txt') as f:
    lines = f.readlines()

protoFields = []
for line in lines:
    m = re.match(r'==> (.*) <==', line)
    if m:
        protoPath = m.group(1)
        protoName = os.path.splitext(os.path.basename(protoPath))[0]
        print ('### %s PROTO' % protoName)
        print ('')
        print ('```')
        print ('%s {' % protoName)
        for field in protoFields:
            m = re.match(r'\s*field\s*([^#]*)#?.*', field)
            if m:
                print ('  %s' % (m.group(1).strip()))
        print ('}')
        print ('```')
        print ('')
        print ('> **File location**: "WEBOTS\_HOME/%s"' % protoPath)
        print ('')
        print ('#### %s PROTO Field Summary' % protoName)
        print ('')
        for field in protoFields:
            m = re.match(r'\s*field\s*[^ ]*\s*([^ ]*)\s*[^#]*#?(.*)', field)
            if m:
                fieldName = m.group(1)
                comment = m.group(2).strip()
                comment = comment[0].lower() + comment[1:]  # First comment letter to lower case
                print ('- `%s` %s' % (fieldName, comment))
        print ('')
        protoFields = []
    else:
        protoFields.append(line)
