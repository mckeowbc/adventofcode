#!/usr/bin/env python

import sys
from hashlib import md5
import re

endloc = (3,3)

directions = ('U','D','L','R')

open_re   = re.compile(r'[bcdef]')
closed_re = re.compile(r'[a0-9]')



def getpos(d,pos):
    if d == 'U':
        newpos = (pos[0] - 1, pos[1])
    elif d == 'D':
        newpos = (pos[0] + 1, pos[1])
    elif d == 'L':
        newpos = (pos[0], pos[1] - 1)
    elif d == 'R':
        newpos = (pos[0], pos[1] + 1)
    else:
        raise ValueError, 'Invalid direction: %s' % d
        
    if any(l < 0 for l in newpos) or \
       any(l > endloc[i] for i,l in enumerate(newpos)):
        raise IndexError,repr(pos)
    return newpos

def walk(salt,path,loc,endloc):
    #print >>sys.stderr,'%s %s' % (path,loc)
    if loc == endloc:
        return [path]
        
    dirs = [True if open_re.match(l) else False
                for l in md5(salt + path).hexdigest()[0:4]]
    sols = []
    for i,d in enumerate(dirs):
        if d:
            direct = directions[i]
            try:  
                newloc = getpos(direct,loc)
                sols += walk(salt,path+direct,newloc,endloc)
            except IndexError:
                pass
    return sols
                
salt = sys.argv[1]
solutions = walk(salt,'',(0,0),endloc)

for sol in sorted(solutions,key=len):
    print len(sol),sol
    

