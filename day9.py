#!/usr/bin/env python

import re
import sys

marker_re = re.compile(r'\((\d+)x(\d+)\)')

fin = sys.argv[1]
data = open(fin).read()
output = ''
loc = 0

while True:
    m = marker_re.search(data[loc:])
    if m:
        output += data[loc:loc+m.start()]
        loc += m.end()

        n = int(m.groups()[0])
        r = int(m.groups()[1])

        output += data[loc:loc+n] * r
        loc += n
    else:
        break

print output
print len(output)
