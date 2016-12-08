#!/usr/bin/env python

import sys

grid = (
    (None,None,1,None,None),
    (None,2,3,4,None),
    (5,6,7,8,9),
    (None,'A','B','C',None),
    (None,None,'D',None,None)
)

pos = [2,0]

num = ''

for dirs in sys.argv[1:]:
    for d in dirs:
        new = pos[:]
        if d == 'U':
            new[0] -= 1
        elif d == 'D':
            new[0] += 1
        elif d == 'R':
            new[1] += 1
        elif d == 'L':
            new[1] -= 1

        for i,p in enumerate(new):
            if p < 0:
                new[i] = 0
            elif p > 4:
                new[i] = 4
        if grid[new[0]][new[1]] is not None:
            pos = new
        print >>sys.stderr,d,pos
    print grid[pos[0]][pos[1]]
    num += str(grid[pos[0]][pos[1]])
print num

