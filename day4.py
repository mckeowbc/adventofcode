#!/usr/bin/env python

import sys
import re

def csort(a,b):
    if a['count'] < b['count']:
        return 1
    elif a['count'] > b['count']:
        return -1
    else:
        return cmp(a['letter'],b['letter'])

room_re = re.compile(r'^((?:[a-z]+-)+)([0-9]+)\[([a-z]{1,5})\]$')

sector_sum = 0

with open(sys.argv[1],'r') as fin:
    for room in fin:
        letters = {}
        room = room.strip()
        m = room_re.match(room)
        if m:
            for letter in m.groups()[0]:
                if 'a' <= letter <= 'z':
                    l = letters.get(letter) or dict()
                    l['letter'] = letter
                    l['count']  = l.get('count',0) + 1
                    letters[letter] = l
            csum =  [l['letter'] for l in sorted(letters.values(),cmp=csort)]
            csum = csum[0:5]
            csum =  ''.join(csum)

            if csum == m.groups()[2]:
                print 'Okay',room
                sector_sum += int(m.groups()[1])
            else:
                print 'Bad',room,csum,m.groups()[2]
        else:
            print 'Bad RE',room

print sector_sum
