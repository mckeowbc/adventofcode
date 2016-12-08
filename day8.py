#!/usr/bin/env python

import sys
import re

grid = [
    ['.' for i in range(50)]
        for j in range(6)
]


def rect(a,b,g):
    for r in range(b):
        for c in range(a):
            grid[r][c] = '#'

def grid_str(g):
    return "\n".join((" ".join(r) for r in g))

def rotate(n,r):
    for _ in range(n):
        r.insert(0,r.pop(-1))

def rotate_col(c,n,g):
    col = [r[c] for r in g]
    rotate(n,col)

    for i,x in enumerate(col):
        g[i][c] = x

def rotate_row(r,n,g):
    rotate(n,g[r])

with open(sys.argv[1],'r') as fin:
    for inst in fin:
        inst = inst.strip()

        if inst.startswith('rect'):
            m = re.search(r'rect\s+(\d+)x(\d+)',inst)

            if not m:
                raise ValueError,inst

            (a,b) = map(int,m.groups())

            rect(a,b,grid)
        elif inst.startswith('rotate row'):
            m = re.search(r'rotate\s+row\s+y=(\d+)\s+by\s+(\d+)',inst)

            if not m:
                raise ValueError, inst
            (r,n) = map(int,m.groups())
            rotate_row(r,n,grid)
        elif inst.startswith('rotate column'):
            m = re.search(r'rotate\s+column\s+x=(\d+)\s+by\s+(\d+)',inst)

            if not m:
                raise ValueError, inst

            (c,n) = map(int,m.groups())
            rotate_col(c,n,grid)

print grid_str(grid)
print grid_str(grid).count('#')
