#!/usr/bin/env python

import sys
from copy import copy

def checksum(h):
    c = []
    for i in range(0,len(h),2):
        pair = h[i:i+2]
        
        if pair[0] == pair[1]:
            c.append(1)
        else:
            c.append(0)
    return c

init = sys.argv[1]
dlen = int(sys.argv[2])

output = [int(i) for i in init]


while len(output) < dlen:
    b = [i^1 for i in reversed(output)]
    output = output + [0] + b



csum = checksum(output[:dlen])

while len(csum) % 2 == 0:
    csum = checksum(csum)
    
    
#print ''.join(map(str,output[:dlen]))
print ''.join(map(str,csum))
    