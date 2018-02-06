txt = """
# testA

- Abc
- DEF
- ghi
klm
nm

testB test
test

- *version* corresponds to the real Nao version. The supported versions are "3.3",
"4.0" and "5.0".

## test C

- Hello world.
- test!

testD...

- test
- test
"""

import re
r = re.sub(r'\n\s*-.+?(?=\n\n)', '', txt, flags=re.S)
r = re.sub(r'\n\s*-.+?(?=\n)', '', r, flags=re.S)
print r
