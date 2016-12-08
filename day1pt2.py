#!/usr/bin/python

import sys
import math

loc = [0,0]
visited = set()
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

    for _ in range(n):
        loc[0] += m[0]
        loc[1] += m[1]
        t = tuple(loc)

        if t in visited:
            print loc
            print sum(map(abs,loc))
            sys.exit(0)
        visited.add(t)

print loc
print sum(map(abs,loc))


