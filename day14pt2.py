#!/usr/bin/env python


from hashlib import md5
import sys
import re

class Key(object):
    def __init__(self,hash,idx,seq):
        self.hash = hash
        self.idx  = idx
        self.seq  = seq
        self.found = None
    def __repr__(self):
        return 'Key(%s, %d, %s, %s)' % (self.hash, self.idx, self.seq, self.found)
        
def stretch(hash,n=2016):
    for i in range(n):
        hash = md5(hash).hexdigest()
    return hash

def printKeys(keys,s='Keys'):
    print '=' * 70
    print s
    for i,key in enumerate(keys):
        print "\t%d\t%s" % (i+1, key)
    #    sorted(keys, key=lambda x:x.idx)))
    print '=' * 70, '\n'
    
triple_re = re.compile(r'([0-9a-f])\1\1')

salt = sys.argv[1]

i = 0
potentials = []
keys       = []

while len(keys) < 64:
    hash = stretch(md5(salt + str(i)).hexdigest())
    while potentials and (i - potentials[0].idx) > 1000:
        p = potentials.pop(0)
    
    done = []
    for idx,p in enumerate(potentials):
        if hash.find(p.seq) >= 0:
            p.found = i
            keys.append(p)
            done.append(idx)
            
    if done:
        printKeys(keys,'Keys')
        for d in sorted(done,reverse=True):
            potentials.pop(d)
        
    m = triple_re.search(hash)
    
    if m:
        potentials.append(Key(hash,i,m.groups()[0] * 5))
    i += 1
    
printKeys(potentials, 'Potentials')
printKeys(keys,'Keys')

print len(keys)
