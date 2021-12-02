#!/usr/bin/env python3
#coding=utf-8
#Created on 02 dec. 2021 - by Daniel González Martínez
#day 1.py

#im late i know

import os, sys

#part 1
increased = 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, line_val = f.readlines(), None
    for index, line in enumerate(lines):
        if line_val != None:
            if line > line_val: 
                increased = increased + 1
        line_val = line

print(increased)

#part 2
increased = 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, packs, last_pack = f.readlines(), [], None
    for index, line in enumerate(lines):
        if index < len(lines)-3:
            packs.append([int(lines[index]), int(lines[index+1]), int(lines[index+2])])

    for pack in packs:
        if last_pack != None:
            if sum(last_pack) < sum(pack): increased = increased + 1
        last_pack = pack
    
print(increased)