#!/usr/bin/env python


import sys

n = int(sys.argv[1])


a = [i for i in range(n)]

b = []

n = len(a)

c = 0

while len(b) < n:
    (t,a) = (a[0:2],a[2:])
    b.extend(t)
    c += 1

    #print 'A',a
    #print 'B',b
    #print 'C',c
    #print

    if len(b) < n:
        (t,b) = ([b[0]], b[1:])
        a.extend(t)
        c += 1

        #print 'A',a
        #print 'B',b
        #print 'C',c
        #print

print c
