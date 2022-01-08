# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:29:03 2022

@author: apan

if you use this
submit in terminal
"python XXX.py <'input file name'.txt>  'output file name'.txt" 

"""

import sys
F=sys.stdin
N=F.readline()
List=F.readline()
print(N.strip("\n"))
print(List.strip("\n").split())

for line in F:
    print(line.strip("\m"))