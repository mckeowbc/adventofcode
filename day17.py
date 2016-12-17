#!/usr/bin/env python

import sys
from hashlib import md5
import re

grid_size = (4,4)

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
        
    if newpos[0] < 0 or  newpos[1] < 0 or \
       newpos[0] >= grid_size[0] or newpos[1] >= grid_size[1]:
        raise IndexError,repr(pos)
    return newpos

def walk(salt,path,loc):
    #print >>sys.stderr,'%s %s' % (path,loc)
    if loc == (3,3):
        return [path]
        
    prefix = md5(salt + path).hexdigest()[0:4]
    dirs = []
    for l in prefix:
        if open_re.match(l):
            dirs.append(True)
        elif closed_re.match(l):
            dirs.append(False)
        else:
            raise RunTimeError,'%s%s:%s' % (salt,path,prefix)
    
    sols = []
    for i,d in enumerate(dirs):
        if d:
            try:
                direct = directions[i]
                newloc = getpos(direct,loc)
                sols += walk(salt,path+direct,newloc)
            except IndexError:
                pass
    return sols
                
salt = sys.argv[1]
solutions = walk(salt,'',(0,0))

for sol in sorted(solutions,key=len):
    print sol,len(sol)
    

