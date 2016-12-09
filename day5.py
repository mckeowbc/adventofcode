#!/usr/bin/env python

import hashlib
import sys

doorid = sys.argv[1]
c = 0
count = 0
passwd = ''

while count < 8:
    h = hashlib.md5(doorid + str(c)).hexdigest()
    if h.startswith('00000'):
        passwd += h[5]
        count = len(passwd)
    c += 1
print passwd
