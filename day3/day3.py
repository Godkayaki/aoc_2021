#!/usr/bin/env python3
#coding=utf-8
#Created on 03 dec. 2021 - by Daniel González Martínez
#day 3.py

#i'll be late on this i know

import os, sys

#part1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines, gamma, epsilon = f.readlines(), "", ""
    for index, line in enumerate(lines[0]):
        zeros, ones = 0, 0
        for index_lines, line_lines in enumerate(lines):
            if line_lines[index] != "\n":
                if int(line_lines[index]) == 0: zeros = zeros + 1
                elif int(line_lines[index]) == 1: ones = ones + 1 
        if zeros > ones: 
            gamma = gamma + "0"
            epsilon = epsilon + "1"
        elif ones > zeros: 
            gamma = gamma + "1"
            epsilon = epsilon + "0"
    g, e = int(gamma, 2), int(epsilon, 2)
    print(g*e)

#part 2
