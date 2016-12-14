#!/usr/bin/env python

import sys

def decode(inst):
    d = inst.split(' ')
    return d[0],d[1:]

fname = sys.argv[1]


with open(fname) as fin:
    insts = [inst.strip() for inst in fin]
    
    
regs = {
    'a': 0,
    'b': 0,
    'c': 1,
    'd': 0
}

i = 0

while i < len(insts):
    print i , insts[i], regs
    inst,oper = decode(insts[i])
    
    if inst == 'jnz':
        if regs.has_key(oper[0]):
            oper1 = regs[oper[0]]
        else:
            oper1 = int(oper[0])
        oper2 = int(oper[1])
        if oper1 != 0:
            i += oper2
        else:
            i += 1
    else:
        if inst == 'cpy':
            if regs.has_key(oper[0]):
                oper1 = regs[oper[0]]
            else:
                oper1 = int(oper[0])
            regs[oper[1]] = oper1
        elif inst == 'inc':
            regs[oper[0]] += 1
        elif inst == 'dec':
            regs[oper[0]] -= 1
        i += 1
        
print regs
    
