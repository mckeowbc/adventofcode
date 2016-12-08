#!/usr/bin/env python

import sys

grid = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)

pos = [1,1]

num = ''

for dirs in sys.argv[1:]:
    for d in dirs:
        if d == 'U':
            pos[0] -= 1
        elif d == 'D':
            pos[0] += 1
        elif d == 'R':
            pos[1] += 1
        elif d == 'L':
            pos[1] -= 1

        for i,p in enumerate(pos):
            if p < 0:
                pos[i] = 0
            elif p > 2:
                pos[i] = 2
        print >>sys.stderr,d,pos
    print grid[pos[0]][pos[1]]
    num += str(grid[pos[0]][pos[1]])
print num

