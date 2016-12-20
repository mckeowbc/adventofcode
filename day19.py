#!/usr/bin/env python

import sys


class Elf(object):
    def __init__(self,n,presents=1):
        self.n = n
        self.presents = presents
    def __repr__(self):
        return 'Elf(%d,%d)' % (self.n,self.presents)
    def __cmp__(self,o):
        return cmp(self.n,o.n)

n = int(sys.argv[1])
elves = [Elf(i) for i in range(1,n+1)]

iteration = 0
remove = set()

while len(remove)+1 < len(elves):
    print iteration,len(remove)
    iteration += 1
    for i in range(len(elves)):
        if i in remove:
            continue
        elif elves[i].presents == 0:
            remove.add(i)
            continue
        j = (i + 1) % len(elves)
        while j != i:
            if elves[j].presents:
                elves[i].presents += elves[j].presents
                elves[j].presents = 0
                break
            j = (j + 1) % len(elves)

for elf in elves:
    if elf.presents:
        print elf
