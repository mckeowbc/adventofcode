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

rows = ['^.^^^.^..^....^^....^^^^.^^.^...^^.^.^^.^^.^^..^.^...^.^..^.^^.^..^.....^^^.^.^^^..^^...^^^...^...^.']

n = int(sys.argv[1])

while len(rows) < n:
    rows.append(row(rows[-1]))
    
tiles = '\n'.join(rows)
print tiles
print tiles.count('.')