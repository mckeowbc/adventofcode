#!/usr/bin/env python

def zeros(l):
    for i in l:
        if i != 0:
            return False
    return True

class Disc(object):
    def __init__(self,d,npos,pos):
        self.d    = d
        self.npos = npos
        self.pos  = pos
        
    def __iter__(self):
        return self
        
    def next(self):
        i = (self.d + self.pos) % self.npos
        self.pos = (self.pos + 1) % self.npos
        return i
        
class Sculpture(object):
    def __init__(self,discs):
        self.discs = discs
    def __iter__(self):
        return self
    def next(self):
        return [d.next() for d in self.discs]
        
s = Sculpture([
    Disc(1,13,11),
    Disc(2,5,0),
    Disc(3,17,11),
    Disc(4,3,0),
    Disc(5,7,2),
    Disc(6,19,17),
    Disc(7,11,0)
])

for i,r in enumerate(s):
    if zeros(r):
        print i
        break