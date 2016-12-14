#!/usr/bin/env python

grid = [
    ['SG','SM','PG','PM'],
    ['TG','RG','RM','CG','CM'],
    ['TM'],
    []
]

def safe(items):
    micros = [m for m in items if m[1] == 'M']
    gens   = [g for g in items if g[1] == 'G'
    
    for m in micros:
        if (m[0] + 'G') not in gens:
            return False
    return True

