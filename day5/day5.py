#!/usr/bin/env python3
#coding=utf-8
#Created on 05 dec. 2021 - by Daniel González Martínez
#day 5.py

import os, sys
from collections import Counter

#part 1
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    segments, res = [line.replace(' -> ', ',') for line in f.read().split('\n')], 0

    straight, diagonal = [], []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2: straight += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
    position_counts = Counter(straight)

print(sum(v > 1 for v in position_counts.values()))

#part 2
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    segments, res = [line.replace(' -> ', ',') for line in f.read().split('\n')], 0

    straight, diagonal = [], []
    for line in segments:
        x1, y1, x2, y2 = map(int, line.split(','))
        (x1, y1), (x2, y2) = sorted([(x1, y1), (x2, y2)])
        if x1 == x2 or y1 == y2: straight += [(x, y) for x in range(x1, x2 + 1) for y in range(y1, y2 + 1)]
        elif y1 < y2: diagonal += [(x, y1 + idx) for idx, x in enumerate(range(x1, x2 + 1))]
        else: diagonal += [(x, y1 - idx) for idx, x in enumerate(range(x1, x2 + 1))]
    position_counts = Counter(straight)
    position_counts += Counter(diagonal)

print(sum(v > 1 for v in position_counts.values()))