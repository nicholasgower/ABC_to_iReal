# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 15:08:40 2024

@author: Nicholas
"""

#Automatically compiles all cython files that I try to import
import pyximport; pyximport.install() 

from ABC_to_iReal.ABCTune import ABCTune


abc=ABCTune(fileDir="abc/Amaranth Waltz.abc")
print(abc)
print()
#print()
#for section in abc.sections:
    #print(section, abc.sections[section])
print(abc.getChords())
print(abc)

print(abc.to_iReal())