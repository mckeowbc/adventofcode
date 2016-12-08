#!/usr/bin/env python

import re
import sys

class Good(Exception):
    pass

class Bad(Exception):
    pass

tls_re = re.compile(r'([a-z])([a-z])\2\1')
sec    = re.compile(r'(?:^|\])([a-z]+)')
hyper  = re.compile(r'\[([a-z]+)\]')

def tls(s):
    m = tls_re.search(s)
    if m:
        substr = s[m.start():m.end()]
        return substr[0] != substr[1]
    return False

with open(sys.argv[1]) as fin:
    for ip in fin:
        ip = ip.strip()

        try:
            for s in hyper.finditer(ip):
                if tls(s.groups()[0]):
                    raise Bad
            for s in sec.finditer(ip):
                if tls(s.groups()[0]):
                    raise Good
            raise Bad
        except Bad:
            print 'Bad',ip
        except Good:
            print 'Good',ip
