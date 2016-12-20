#!/usr/bin/env python

import sys


n = int(sys.argv[1])
elves = [i for i in range(1,n+1)]

iteration = 0
remove = set()

nelves = len(elves)

while len(elves) > 1:
    iteration += 1
    
    for i in range(len(elves)): 
        if i >= len(elves):
            break
        print elves[i], iteration,nelves,elves # , [elf for elf in elves if elf != 0]
        
        target = ((len(elves) / 2) + i) % len(elves)
        elves.pop(target)
        
print elves