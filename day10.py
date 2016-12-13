#!/usr/bin/env python

import sys
import re

goes_re  = re.compile(r'^value\s+(\d+)\s+goes\s+to\s+bot\s+(\d+)')
gives_re = re.compile(r'^bot\s+(\d+)\s+gives\s+low\s+to\s+(bot|output)\s+(\d+)\s+and\s+high\s+to\s+(bot|output)\s+(\d+)')


class Bot(object):
    def __init__(self,n,values=None):
        self.__num = int(n)
        self.__values = values if values else []

    def goes(self,val):
        if len(self.__values) == 2:
            raise RuntimeError,'Bot %d is already full (%s)' % (self.__num, val)
        self.__values = sorted(self.__values + [val])

    def gives(self,bl,bh):
        if self.can_give() and bl.can_goes() and bh.can_goes():
            bl.goes(self.__values[0])
            bh.goes(self.__values[1])
            self.__values = []
        else:
            raise RuntimeError,'%s cannot give to %s and %s' % (self, bl, bh)
        
    def can_give(self):
        return len(self.__values) == 2
        
    def can_goes(self):
        return len(self.__values) < 2
    
    def __repr__(self):
        if self.__values:
            return "Bot(%d,values=%s)" % (self.num,self.__values)
        else:
            return "Bot(%d)" % self.num
        
    @property
    def num(self):
        return self.__num
        
    @property
    def values(self):
        return tuple(self.__values)
        
class Output(object):
    def __init__(self, n, values=None):
        self.__num = int(n)
        self.__values = values if values else []
        
    @property
    def values(self):
        return tuple(self.__values)
        
    def goes(self,val):
        self.__values.append(val)
        
    def can_goes(self):
        return True
        
    def can_give(self):
        return False
        
    def __repr__(self):
        return 'Output(%d,values=%s)' % (self.__num, self.__values)

class Inst(object):
    def __init__(self, bot):
        self.bot = bot
        
class Goes(Inst):
    def __init__(self, bot, val):
        Inst.__init__(self,bot)
        self.val = int(val)
        
    def run(self):
        self.bot.goes(self.val)
        
class Gives(Inst):
    def __init__(self, bot, bl, bh):
        Inst.__init__(self,bot)
        self.bl = bl
        self.bh = bh
        
    def run(self):
        self.bot.gives(self.bl,self.bh)
        
def get_bot(n, bots):
    if not bots.has_key(n):
        bots[n] = Bot(n)
    return bots[n]
    
def get_output(n, output):
    if not output.has_key(n):
        output[n] = Output(n)
    return output[n]

def decode(inst, bots, outputs):
    m = goes_re.search(inst)
    
    if m:
        return Goes(get_bot(m.groups()[1], bots),m.groups()[0])
        
    m = gives_re.search(inst)
    
    if m:
        bot = get_bot(m.groups()[0],bots)
        bl  = get_bot(m.groups()[2],bots) if m.groups()[1] == 'bot' else get_output(m.groups()[2],outputs)
        bh  = get_bot(m.groups()[4],bots) if m.groups()[3] == 'bot' else get_output(m.groups()[4],outputs)
        return Gives(bot,bl,bh)
        
    raise RuntimeError,'Could not decode: %s' % inst


if __name__ == '__main__':
    fname   = sys.argv[1]
    stack   = []
    bots    = {}
    outputs = {}
    with open(sys.argv[1]) as fin:
        for line in fin:
            stack.append(decode(line,bots,outputs))
            
    while stack:
        for i, inst in enumerate(stack):
            #if inst.bot.values == (17,61):
            #    print inst.bot
            #    sys.exit(0)
            try:
                inst.run()
                break
            except RuntimeError,e:
                #print >>sys.stderr,e
                pass
        stack.pop(i)
        
    for bot in bots.values():
        print bot
        
    for output in sorted(outputs.keys(),key=int):
        print outputs[output]
                