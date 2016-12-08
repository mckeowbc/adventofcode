#! /usr/bin/env python

import sys

reps = []

def mode(l):
    return max(set(l),key=l.count)

with open(sys.argv[1],'r') as fin:
    for line in fin:
        line = line.strip()

        for i,l in enumerate(line):
            if i > len(reps)-1:
                reps.append([])
            reps[i].append(l)

print ''.join((mode(l) for l in reps))
