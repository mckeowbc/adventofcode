#!/usr/bin/env python

import sys
import re
import itertools

input = sys.argv[1]

with open(input,'r') as fin:
    for t in fin:
        t = t.strip()
        sides = map(int,re.split(r'\s+',t))

        try:
            for p in itertools.permutations(sides):
                if p[0] >= sum(p[1:]):
                    raise ValueError
            print 'Okay',sides
        except ValueError:
            print 'Bad',sides

