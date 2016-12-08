#!/usr/bin/env python

import re
import sys

class Good(Exception):
    pass

class Bad(Exception):
    pass

ssl_re = re.compile(r'([a-z])([a-z])\1')
sec    = re.compile(r'(?:^|\])([a-z]+)')
hyper  = re.compile(r'\[([a-z]+)\]')

def ssl(s):
    l = []
    while s:
        m = ssl_re.search(s)
        if not m:
            break
        l.append(s[m.start():m.end()])
        s = s[m.start()+1:]
    return l

with open(sys.argv[1]) as fin:
    for ip in fin:
        ip = ip.strip()

        try:
            abas = []
            for s in sec.finditer(ip):
                abas.extend(ssl(s.groups()[0]))
            if not abas:
                raise Bad

            for aba in abas:
                bab_re = re.compile(aba[1] + aba[0] + aba[1])
                for s in hyper.finditer(ip):
                    if bab_re.search(s.groups()[0]):
                        raise Good
            raise Bad
        except Bad:
            print 'Bad',ip
        except Good:
            print 'Good',ip
