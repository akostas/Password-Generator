# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 23:13:36 2021

@author: Konstantinos
"""

import random

aps = []

length = int(input('Set the length of the password: '))
symbols = input('Do you want to include symbols?(Y|y|N|n) ')
numbers = input('Do you want to include numbers?(Y|y|N|n) ')
capLets = input('Do you want to include capital leters?(Y|y|N|n) ')
smaLets = input('Do you want to include small letters?(Y|y|N|n) ')
excSim = input('Do you want to exclude similar characters?(Y|y|N|n) ')
excAmb = input('Do you want to exclude amgiuous characters?(Y|y|N|n) ')

if symbols in 'Yy':
    aps.extend([i for i in range(33,48)])
    aps.extend([i for i in range(58,65)])
    aps.extend([i for i in range(91,97)])
    aps.extend([i for i in range(123,127)])
    
if numbers in 'Yy':
    aps.extend([i for i in range(48,58)])
    
if capLets in 'Yy':
    aps.extend([i for i in range(65,91)])
    
if smaLets in 'Yy':
    aps.extend([i for i in range(97,123)])
    
if excSim in 'Yy':
    aps.extend([i for i in [105, 73, 108, 76, 49, 111, 48, 79]])
    
if excAmb in 'Yy':
    aps.extend([123, 124, 91, 93, 40, 41, 47, 92, 96, 126, 39, 34, 44, 59, 58, 46, 60, 62])

random.shuffle(aps)
fc = random.sample(aps, length)
    
fs = ''
for i in fc:
    fs += chr(i)

print(fs)
    