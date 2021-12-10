#!/usr/bin/env python3
#coding=utf-8
#Created on 10 dec. 2021 - by Daniel González Martínez
#day 10.py

import os, sys, copy

#part1
#openList, closeList = ["[", "{", "(", "<"], ["]", "}", ")", ">"]
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()
    ups = ['(', '{', '[', "<", ')', '}', ']', ">"]
    for index, line in enumerate(lines):
        counters = [0, 0, 0, 0, 0, 0, 0, 0]
        real_line = line.rstrip("\n")
        for i in real_line:
            ind = ups.index(i)
            counters[ind] += 1
        print(counters)
