#!/usr/bin/env python

import sys


n = int(sys.argv[1])
elves = [i for i in range(1,n+1)]

iteration = 0
remove = set()



while len(elves) > 1:
    print iteration
    iteration += 1
    nelves = len(elves)
    
    target = (len(elves) / 2)
    
    for i in range(len(elves)):
        if elves[i] == 0:
            continue
        #print i,target,elves[i], elves[target],[e for e in elves if e != 0] # , [elf for elf in elves if elf != 0]
        
        elves[target] = 0
        
        if nelves % 2 == 0:
            target = (target + 1) % len(elves)
        else:
            target = (target + 2) % len(elves)
        nelves -= 1
        
    elves = [e for e in elves if e != 0]
        
print elves