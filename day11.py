#!/usr/bin/env python

grid = [
    ['SG','SM','PG','PM'],
    ['TG','RG','RM','CG','CM'],
    ['TM'],
    []
]


grid = [4,5,1,0]

total = sum(grid)

count = 0

while grid[-1] < total:
