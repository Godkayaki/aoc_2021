#!/usr/bin/env python3
#coding=utf-8
#Created on 09 dec. 2021 - by Daniel González Martínez
#day 9.py

#this is a fucking mess but i don't care anymore honestly

import os, sys

#part 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, lines_vals, res = f.readlines(), [], []
    for index, line in enumerate(lines):
        lines_vals.append(list(line.rstrip("\n")))

    for index, line in enumerate(lines_vals):
        up, down = None, None
        if index == 0: up = False
        elif index == len(lines_vals): down = False
        
        for index_line, val in enumerate(line):
            left, right, vals_tocalc = None, None, []
            if index_line == 0: left = False
            elif index_line == len(line): right = False

            #set vals
            try: 
                if left != False: vals_tocalc.append(int(line[index_line-1]))
            except: pass
            try: 
                if up != False: vals_tocalc.append(int(lines_vals[index-1][index_line]))
            except: pass
            try: 
                if right != False: vals_tocalc.append(int(line[index_line+1]))
            except: pass
            try: 
                if down != False: vals_tocalc.append(int(lines_vals[index+1][index_line]))
            except: pass

            a = True
            for num in vals_tocalc: 
                if int(val) >= num: a = False
            if a != False: res.append(int(val)+1)

print(sum(res))