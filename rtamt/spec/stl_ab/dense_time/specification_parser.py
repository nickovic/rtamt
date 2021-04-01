# -*- coding: utf-8 -*-
"""
Created on Tue Jul 23 21:38:29 2019

@author: NickovicD
"""

from rtamt.spec.stl.discrete_time.specification_parser import STLSpecificationParser

class STLDenseTimeSpecificationParser(STLSpecificationParser):
    
    def __init__(self, spec):
        super(STLDenseTimeSpecificationParser, self).__init__(spec)

    def visitIntervalTimeLiteral(self, ctx):
        text = ctx.literal().getText()
        out = float(text)

        if ctx.unit() != None:
            unit = ctx.unit().getText()
            if (unit == 'ps'):
                out = out * 1e-12
            elif (unit == 'ms'):
                out = out * 1e-3
            elif (unit == 'us'):
                out = out * 1e-6
            elif (unit == 'ns'):
                out = out * 1e-9
            else:
                pass

        return out



