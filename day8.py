#!/usr/bin/env python

import sys
import re

def rotate(n,r):
    for _ in range(n):
        r.insert(0,r.pop(-1))

class Grid(object):
    def __init__(self):
        self.__grid = [
            [' ' for i in range(50)]
                for j in range(6)
        ]

    def rect(self,a,b):
        for r in range(b):
            for c in range(a):
                self.__grid[r][c] = '#'

    def __str__(self):
        return "\n".join((" ".join(r) for r in self.__grid))

    def rotate_col(self,c,n):
        col = [r[c] for r in self.__grid]
        rotate(n,col)

        for i,x in enumerate(col):
            self.__grid[i][c] = x

    def rotate_row(self,r,n):
        rotate(n,self.__grid[r])

with open(sys.argv[1],'r') as fin:
    grid = Grid()
    for inst in fin:
        inst = inst.strip()

        if inst.startswith('rect'):
            m = re.search(r'rect\s+(\d+)x(\d+)',inst)

            if not m:
                raise ValueError,inst

            (a,b) = map(int,m.groups())

            grid.rect(a,b)
        elif inst.startswith('rotate row'):
            m = re.search(r'rotate\s+row\s+y=(\d+)\s+by\s+(\d+)',inst)

            if not m:
                raise ValueError, inst
            (r,n) = map(int,m.groups())
            grid.rotate_row(r,n)
        elif inst.startswith('rotate column'):
            m = re.search(r'rotate\s+column\s+x=(\d+)\s+by\s+(\d+)',inst)

            if not m:
                raise ValueError, inst

            (c,n) = map(int,m.groups())
            grid.rotate_col(c,n)

print grid
print str(grid).count('#')
