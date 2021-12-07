#!/usr/bin/env python3
#coding=utf-8
#Created on 07 dec. 2021 - by Daniel González Martínez
#day 7.py

import os, sys

#part 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, fuel_lower = f.readlines(), 0
    for index, line in enumerate(lines):
        start_vals = list(map(int, line.split(',')))
        max_v, min_v = max(start_vals), min(start_vals)

    for i in range(min_v, max_v):
        new_vals = []
        for number in start_vals:
            if number > i: new_vals.append(number-i)
            else:  new_vals.append(i-number)
        
        if sum(new_vals) < fuel_lower or fuel_lower == 0:
            fuel_lower = sum(new_vals)
    
print(fuel_lower)

#part 2
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, fuel_lower = f.readlines(), 0
    for index, line in enumerate(lines):
        start_vals = list(map(int, line.split(',')))
        max_v, min_v = max(start_vals), min(start_vals)

    for i in range(min_v, max_v):
        new_vals = []
        for number in start_vals:
            if number > i: 
                t = 0
                for x in range(1, (number-i)+1): t += x
                new_vals.append(t)
            else:
                t = 0
                for x in range(1, (i-number)+1): t += x
                new_vals.append(t)
        
        if sum(new_vals) < fuel_lower or fuel_lower == 0:
            fuel_lower = sum(new_vals)
    
print(fuel_lower)