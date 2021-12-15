#!/usr/bin/env python3
#coding=utf-8
#Created on 15 dec. 2021 - by Daniel González Martínez
#day 15.py

import os, sys, copy

#part 1
lines, res = [] , 0
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    for line in f:
        lines.append(line.rstrip("\n"))

