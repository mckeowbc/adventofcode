#!/usr/bin/env python

import hashlib
import sys

doorid = sys.argv[1]
c = 0
passwd = ''

while len(passwd) < 8:
    h = hashlib.md5(doorid + str(c)).hexdigest()

    if h[0:5] == '00000':
        passwd += h[5]
    c += 1
print passwd
