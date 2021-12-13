#!/usr/bin/env python3
#coding=utf-8
#Created on 13 dec. 2021 - by Daniel González Martínez
#day 11.py

#I'm late i know weekend went crazy

import os, sys, copy

#part 1
lines, flashes, steps = [] , 0, 100
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    for line in f:
        line_stripped = line.rstrip("\n")
        lines.append(list(map(int, line_stripped)))
    
    for step in range(0, steps):
        for y, row_val in enumerate(lines):
            for x, single_val in enumerate(lines[0]):
                if lines[y][x] == 9:
                    lines[y][x] = 'flash'
                else:
                    lines[y][x] += 1
        break
    
    for line in lines: print(line)