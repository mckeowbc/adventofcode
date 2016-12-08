#!/usr/bin/env python

import hashlib
import sys

doorid = sys.argv[1]
c = 0
found = 0
passwd = [None for i in range(8)]

while found < 8:
    h = hashlib.md5(doorid + str(c)).hexdigest()

    if h[0:5] == '00000':
        try:
            pos = int(h[5])
            if pos < len(passwd) and passwd[pos] is None:
                passwd[pos] = h[6]
                found += 1
                print c,passwd
        except:
            pass
    c += 1
print ''.join(passwd)
