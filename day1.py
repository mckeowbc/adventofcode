#!/usr/bin/python

import sys
import math

start = [0,0]
direction = 0

for dir in sys.argv[1:]:
    dir = dir.replace(',','')
    d = dir[0]
    n = int(dir[1:])

    if d == 'R':
        direction += 90
    else:
        direction -= 90

    rads = math.radians(direction)

    m = [int(math.sin(rads)), int(math.cos(rads))]

    start[0] += m[0] * n
    start[1] += m[1] * n

print start
print sum(map(abs,start))
