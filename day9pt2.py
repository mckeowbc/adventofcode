#!/usr/bin/env python

import re
import sys

marker_re = re.compile(r'\((\d+)x(\d+)\)')


def chunks(buf):
    m = marker_re.search(buf)

    while m:
        if m.start():
            yield buf[0:m.start()]
        n = int(m.groups()[0])
        r = int(m.groups()[1])
        yield buf[m.start():m.end()+n]
        buf = buf[m.end()+n:]
        m = marker_re.search(buf)
    yield buf

def chunk_len(buf):
    m = marker_re.search(buf)

    if m:
        n = int(m.groups()[0])
        r = int(m.groups()[1])
        
        #print m.start(), m.end(), n, r, buf

        return m.start() + chunk_len(buf[m.end():m.end()+n]) * r + chunk_len(buf[m.end()+n:])
    else:
        return len(buf)


fin = sys.argv[1]
data = open(fin).read()
loc = 0
olen = 0
obuf = ''

for chunk in chunks(data):
    chunk = chunk.strip()
    llen = chunk_len(chunk)
    print chunk, llen
    olen += llen
print olen
