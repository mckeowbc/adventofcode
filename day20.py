#!/usr/bin/env python

import sys
from copy import copy

def rcombine(oldr):
    cur = copy(oldr[0])
    newr = []
    for r in oldr[1:]:
        if cur[1]+1 >= r[0]:
            if cur[1] < r[1]:
                cur[1] = r[1]
        else:
            newr.append(cur)
            cur = copy(r)
    newr.append(cur)
    return newr

fname = sys.argv[1]

ranges = (list(map(int,l.strip().split('-'))) for l in open(fname).readlines())

sranges = sorted(ranges,key=lambda x:x[0])
crange  = rcombine(sranges)


while len(crange) < len(sranges):
    sranges = sorted(crange,key=lambda x:x[0])
    crange  = rcombine(sranges)

cur = crange[0]

for r in crange[1:]:
    for ip in range(cur[1]+1,r[0]):
        print ip
    cur = r