#!/usr/bin/env python

import sys


traps = set((
    '^^.',
    '.^^',
    '^..',
    '..^',
))

def row(r):
    wr = '.' + r + '.'
    nr = ''
    for i in range(1,len(r)+1):
        if wr[i-1:i+2] in traps:
            nr += '^'
        else:
            nr += '.'
    return nr

currow = '^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.'

n = int(sys.argv[1])
i = 1
count = currow.count('.')

for i in range(1,n):
    if i % 1000 == 0:
        print i
    currow = row(currow)
    count += currow.count('.')

print count