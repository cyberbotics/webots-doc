"""Extract MD from fields.txt."""
# Generate "robots.txt": 'find projects/robots -name *.proto' + manual cleanup
# Generate "fields.txt": 'cat robots.txt | xargs head -60 | grep "proto\|field" > fields.txt' + manual cleanup

import os
import re

with open('fields.txt') as f:
    lines = f.readlines()

protoFields = []
protoPath = ''
protoName = ''

def flush_proto():
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
    print ('#### %s Field Summary' % protoName)
    print ('')
    for field in protoFields:
        m = re.match(r'\s*field\s*[^ ]*\s*([^ ]*)\s*[^#]*#?(.*)', field)
        if m:
            fieldName = m.group(1)
            comment = m.group(2).strip()

            m = re.match(r'Is `([^`]*)`\.', comment)
            if m:
                comment = 'Inherited from `%s` node.' % (m.group(1).split('.')[0])

            def replacement(match):
                m = match.group(1)
                mL = m[0].lower() + m[1:]
                return '[%s](../reference/%s.md)' % (m, mL)

            comment = re.sub(r'`([^\.`]*)(\.[^`]*)?`', replacement, comment)
            print ('- `%s`: %s' % (fieldName, comment))
            print ('')
    print ('')


for line in lines:
    m = re.match(r'==> (.*) <==', line)
    if m:
        if protoPath:
            flush_proto()
        protoPath = m.group(1)
        protoName = os.path.splitext(os.path.basename(protoPath))[0]
        protoFields = []
    else:
        protoFields.append(line)
flush_proto()
