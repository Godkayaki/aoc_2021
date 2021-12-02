#!/usr/bin/env python3
#coding=utf-8
#Created on 02 dec. 2021 - by Daniel González Martínez
#day 2.py

#i'll be on time today bro

import os, sys

#part 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, line_val, horizontal, depth = f.readlines(), None, 0, 0
    for index, line in enumerate(lines):
        vals = line.split()
        if vals[0] == "forward": horizontal = horizontal + int(vals[1])
        elif vals[0] == "down": depth = depth + int(vals[1])
        elif vals[0] == "up": depth = depth - int(vals[1])
print(horizontal*depth)

#part 2
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, line_val, horizontal, depth, aim = f.readlines(), None, 0, 0, 0
    for index, line in enumerate(lines):
        vals = line.split()
        if vals[0] == "forward": 
            horizontal = horizontal + int(vals[1])
            if aim != 0: depth = depth + (int(vals[1]) * aim)
        elif vals[0] == "down": aim = aim + int(vals[1])
        elif vals[0] == "up": aim = aim - int(vals[1])
print(horizontal*depth)