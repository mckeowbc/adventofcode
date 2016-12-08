#!/usr/bin/env python

import sys
import re
import itertools

input = sys.argv[1]

buf = [[],[],[]]

with open(input,'r') as fin:
    for t in fin:
        t = t.strip()
        sides = map(int,re.split(r'\s+',t))

        for i,s in enumerate(sides):
            buf[i].append(s)

        if len(buf[0]) == 3:
            for tri in buf:
                try:
                    for p in itertools.permutations(tri):
                        if p[0] >= sum(p[1:]):
                            raise ValueError
                    print 'Okay',tri
                except ValueError:
                    print 'Bad',tri
            buf = [[],[],[]]

