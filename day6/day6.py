#!/usr/bin/env python3
#coding=utf-8
#Created on 06 dec. 2021 - by Daniel González Martínez
#day 6.py

import os, sys

days = 256

#part 1 & 2
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    #get list from 0-8 to count repetitions for each value
    counts = [0] * 9
    for n in f.read().split(','):
        counts[int(n)] += 1
    
    #iterate days and move values by -1
    for day in range(days):
        births, *counts = counts + [0]
        counts[6] += births
        counts[8] += births

    print(sum(counts))