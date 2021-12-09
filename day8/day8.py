#!/usr/bin/env python3
#coding=utf-8
#Created on 08 dec. 2021 - by Daniel González Martínez
#day 8.py

import os, sys

#part 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, unique_vals_c, unique_e = f.readlines(), [7, 2, 3, 4], 0
    for index, line in enumerate(lines):
        delimited_vals = line.split('|')
        del_delimited_vals = delimited_vals[1].split(' ')
        for val in del_delimited_vals:
            if len(val.rstrip("\n")) in unique_vals_c:
                unique_e += 1

print(unique_e)

pos = [0, 2, 3, 5, 6, 9]
vals = ["cagedb", "gcdfa", "fbcad", "cdfbe", "cdfgeb", "cefabd"]

#part 2
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, unique_vals_c = f.readlines(), [7, 2, 3, 4]
    for index, line in enumerate(lines):
        delimited_vals = line.split('|')
        del_delimited_vals = delimited_vals[1].split(' ')
        del_delimited_vals.pop(0)
        for val in del_delimited_vals:
            new_val = ""
            if len(val.rstrip("\n")) in unique_vals_c:
                new_val = new_val + str(len(val.rstrip("\n")))
            else:
                for index, pos in enumerate(vals):
                    print(''.join(sorted(pos)), ''.join(sorted(val.rstrip("\n"))))
                    if ''.join(sorted(pos)) == ''.join(sorted(val.rstrip("\n"))):
                        new_val = new_val + str(index)
                        break
            print(new_val)

#print(unique_e)